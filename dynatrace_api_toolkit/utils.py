import datetime
from typing import List

import pandas as pd


def get_date_to_timestamp(cdate: str) -> int:
    """Convert a date string in d.%m.%Y %H:%M format to milliseconds since epoch."""
    dt_obj = datetime.datetime.strptime(cdate, "%d.%m.%Y %H:%M")
    return int(dt_obj.timestamp() * 1000)


def get_timestamp_to_date(millisec: int) -> str:
    """Convert milliseconds since epoch to a readable datetime string."""
    sec = millisec / 1000
    return datetime.datetime.fromtimestamp(sec).strftime("%Y-%m-%d %H:%M:%S")


def load_entity_ids_from_excel(path: str, sheet_name=0, column_name: str = "entityId") -> List[str]:
    """Read an Excel file and return a list of entity IDs from the specified column."""
    df = pd.read_excel(path, sheet_name=sheet_name)
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in Excel file")
    return [str(value) for value in df[column_name].dropna().tolist()]
