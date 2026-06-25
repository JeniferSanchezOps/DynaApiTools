import json
from typing import Any, Dict, List, Optional

import pandas as pd
import requests

from .utils import load_entity_ids_from_excel


def build_url(base_url: str, path: str, query: Optional[Dict[str, Any]] = None) -> str:
    url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
    if query:
        query_string = "&".join(
            f"{key}={requests.utils.quote(str(value), safe='')}" for key, value in query.items()
        )
        url = f"{url}?{query_string}"
    return url


def build_headers(api_token: str) -> Dict[str, str]:
    return {
        "accept": "application/json; charset=utf-8",
        "Authorization": f"Api-Token {api_token}",
        "Content-Type": "application/json; charset=utf-8",
    }


def post_settings_objects(
    payload: Any,
    api_token: str,
    base_url: str,
    validate_only: bool = False,
) -> requests.Response:
    params = {"validateOnly": "false"} if not validate_only else {"validateOnly": "true"}
    url = build_url(base_url, "/api/v2/settings/objects", params)
    body = json.dumps(payload) if not isinstance(payload, str) else payload
    response = requests.post(url=url, headers=build_headers(api_token), data=body)
    response.raise_for_status()
    return response


def disable_host_monitoring(
    host_id: str,
    api_token: str,
    base_url: str,
    schema_version: str = "1.3",
    validate_only: bool = False,
) -> requests.Response:
    payload = [
        {
            "schemaId": "builtin:host.monitoring",
            "schemaVersion": schema_version,
            "scope": host_id,
            "value": {"enabled": False, "autoInjection": True},
        }
    ]
    return post_settings_objects(payload, api_token=api_token, base_url=base_url, validate_only=validate_only)


def fetch_oneagents(
    hostgroup_id: str,
    from_ts: int,
    to_ts: int,
    api_token: str,
    base_url: str,
    os_type: str = "LINUX",
    availability_state: str = "MONITORED",
    include_details: bool = True,
) -> List[Dict[str, Any]]:
    path = "/api/v1/oneagents"
    query = {
        "includeDetails": str(include_details).lower(),
        "hostGroupId": hostgroup_id,
        "osType": os_type,
        "availabilityState": availability_state,
        "from": from_ts,
        "to": to_ts,
    }
    url = build_url(base_url, path, query)
    response = requests.get(url=url, headers=build_headers(api_token), verify=False)
    response.raise_for_status()
    data = response.json()
    hosts = data.get("hosts", [])
    next_page_key = data.get("nextPageKey")

    while next_page_key:
        query["nextPageKey"] = next_page_key
        url = build_url(base_url, path, query)
        page_response = requests.get(url=url, headers=build_headers(api_token), verify=False)
        page_response.raise_for_status()
        page_data = page_response.json()
        hosts.extend(page_data.get("hosts", []))
        next_page_key = page_data.get("nextPageKey")

    return hosts


def extract_host_info(hosts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for host in hosts:
        info = host.get("hostInfo", {})
        rows.append(
            {
                "consumedHostUnits": info.get("consumedHostUnits"),
                "osType": info.get("osType"),
                "discoveredName": info.get("discoveredName"),
                "ipAddresses": info.get("ipAddresses"),
                "entityId": info.get("entityId"),
            }
        )
    return rows


def save_hosts_to_excel(hosts: List[Dict[str, Any]], destination: str) -> None:
    df = pd.DataFrame(hosts)
    df.to_excel(destination, index=False, sheet_name="Hosts")


def load_entity_ids(path: str, sheet_name=0, column_name: str = "entityId") -> List[str]:
    return load_entity_ids_from_excel(path, sheet_name=sheet_name, column_name=column_name)
