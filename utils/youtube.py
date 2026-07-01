import re
import yt_dlp

from utils.helpers import (
    format_duration,
    format_upload_date
)


def extract_video_id(url):
    """
    Extract YouTube Video ID from different URL formats.
    """

    patterns = [
        r"(?:v=)([0-9A-Za-z_-]{11})",
        r"(?:youtu\.be/)([0-9A-Za-z_-]{11})",
        r"(?:embed/)([0-9A-Za-z_-]{11})"
    ]

    for pattern in patterns:

        match = re.search(pattern, url)

        if match:
            return match.group(1)

    return None


def get_video_info(url):
    """
    Fetch YouTube metadata using yt-dlp.
    """

    ydl_opts = {
        "quiet": True,
        "skip_download": True
    }

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(url, download=False)

            return {

                "original_url": url,

                "video_id": extract_video_id(url),

                "title": info.get("title", "Unknown"),

                "channel": info.get("uploader", "Unknown"),

                "views": f"{info.get('view_count', 0):,}",

                "likes": f"{info.get('like_count', 0):,}",

                "comments": f"{info.get('comment_count', 0):,}",

                "duration": format_duration(
                    info.get("duration", 0)
                ),

                "upload_date": format_upload_date(
                    info.get("upload_date")
                ),

                "thumbnail": info.get("thumbnail"),

                "description": info.get("description", "")

            }

    except Exception as e:

        return {
            "error": str(e)
        }