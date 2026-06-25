import argparse
import os

from dynatrace_api_toolkit.client import extract_host_info, fetch_oneagents, save_hosts_to_excel
from dynatrace_api_toolkit.config import DT_API_TOKEN, DT_BASE_URL
from dynatrace_api_toolkit.utils import get_date_to_timestamp


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Dynatrace OneAgent host data for a host group.")
    parser.add_argument("--hostgroup", required=True, help="Host group ID, for example HOST_GROUP-xxxx")
    parser.add_argument("--from", dest="from_time", required=True, help="Start time in format dd.MM.YYYY HH:MM")
    parser.add_argument("--to", dest="to_time", required=True, help="End time in format dd.MM.YYYY HH:MM")
    parser.add_argument("--output", required=True, help="Excel output path")
    parser.add_argument("--token", help="Dynatrace API token")
    parser.add_argument("--base-url", default=DT_BASE_URL, help="Dynatrace base URL")
    args = parser.parse_args()

    api_token = args.token or os.getenv("DT_API_TOKEN") or DT_API_TOKEN
    if not api_token:
        raise SystemExit("Error: DT API token is required in --token or DT_API_TOKEN environment variable.")

    from_ts = get_date_to_timestamp(args.from_time)
    to_ts = get_date_to_timestamp(args.to_time)
    hosts = fetch_oneagents(
        hostgroup_id=args.hostgroup,
        from_ts=from_ts,
        to_ts=to_ts,
        api_token=api_token,
        base_url=args.base_url,
    )
    rows = extract_host_info(hosts)
    save_hosts_to_excel(rows, args.output)
    print(f"Saved {len(rows)} host rows to {args.output}")


if __name__ == "__main__":
    main()
