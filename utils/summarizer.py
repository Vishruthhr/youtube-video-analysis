import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Use Gemini 2.5 Flash
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary(transcript):
    """
    Generate an AI summary of the transcript.
    """

    if not transcript:
        return "Transcript not available."

    if transcript.startswith("Transcript not available"):
        return transcript

    try:

        # Limit very long transcripts
        transcript = transcript[:12000]

        prompt = f"""
You are an AI assistant.

Summarize the following YouTube video transcript.

Requirements:
- Keep the summary between 150 and 250 words.
- Use simple English.
- Highlight the main topics.
- Return only the summary.

Transcript:

{transcript}
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:

        return f"Summary generation failed: {str(e)}"