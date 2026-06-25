import argparse
import os

from dynatrace_api_toolkit.client import disable_host_monitoring, load_entity_ids
from dynatrace_api_toolkit.config import DT_API_TOKEN, DT_BASE_URL


def main() -> None:
    parser = argparse.ArgumentParser(description="Disable Dynatrace host monitoring using a list of entity IDs from Excel.")
    parser.add_argument("--excel", required=True, help="Excel file path containing entityId column")
    parser.add_argument("--token", help="Dynatrace API token")
    parser.add_argument("--base-url", default=DT_BASE_URL, help="Dynatrace base URL")
    parser.add_argument("--validate-only", action="store_true", help="Do not persist changes")
    args = parser.parse_args()

    api_token = args.token or os.getenv("DT_API_TOKEN") or DT_API_TOKEN
    if not api_token:
        raise SystemExit("Error: DT API token is required in --token or DT_API_TOKEN environment variable.")

    entity_ids = load_entity_ids(args.excel)
    for host_id in entity_ids:
        response = disable_host_monitoring(
            host_id=host_id,
            api_token=api_token,
            base_url=args.base_url,
            validate_only=args.validate_only,
        )
        print(f"Host {host_id}: {response.status_code}")


if __name__ == "__main__":
    main()
