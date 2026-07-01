from youtube_transcript_api import YouTubeTranscriptApi

video_id = "rfscVS0vtbw"

try:

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    print("Transcript fetched successfully!\n")

    for line in transcript[:5]:
        print(line.text)

except Exception as e:

    print(type(e).__name__)

    print(e)