import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    """
    Extract YouTube video ID from different URL formats.
    """

    patterns = [
        r"(?:v=)([0-9A-Za-z_-]{11})",
        r"(?:youtu\.be/)([0-9A-Za-z_-]{11})",
        r"(?:embed/)([0-9A-Za-z_-]{11})",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def get_transcript(url):
    """
    Returns transcript text if available.
    """

    video_id = extract_video_id(url)

    if video_id is None:
        return "Invalid YouTube URL."

    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        transcript_text = ""

        for line in transcript:
            transcript_text += line.text + " "

        return transcript_text.strip()

    except Exception as e:
        return f"Transcript not available.\n\n{str(e)}"