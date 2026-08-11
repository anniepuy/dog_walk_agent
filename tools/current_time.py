from datetime import datetime
from zoneinfo import ZoneInfo

def get_current_time(timezone: str) -> str:
    """Return the current local date and time for an IANA timezone."""
    return datetime.now(
        ZoneInfo(timezone)
    ).isoformat(timespec="seconds")

