import os

DEFAULT_BASE_URL = "https://ejemplo.live.dynatrace.com"

DT_API_TOKEN = os.getenv("DT_API_TOKEN", "")
DT_BASE_URL = os.getenv("DT_BASE_URL", DEFAULT_BASE_URL)
