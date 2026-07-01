from datetime import datetime


def format_duration(seconds):
    """
    Convert seconds into:
    45s
    4m 32s
    1h 05m 10s
    """

    try:
        seconds = int(seconds)
    except (TypeError, ValueError):
        return "Unknown"

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    if hours > 0:
        return f"{hours}h {minutes:02d}m {remaining_seconds:02d}s"

    if minutes > 0:
        return f"{minutes}m {remaining_seconds:02d}s"

    return f"{remaining_seconds}s"


def format_upload_date(date_string):
    """
    Convert:
        20180711
    into:
        11 July 2018
    """

    if not date_string:
        return "Unknown"

    try:
        return datetime.strptime(
            date_string,
            "%Y%m%d"
        ).strftime("%d %B %Y")

    except Exception:

        return date_string