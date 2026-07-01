import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def extract_keywords(transcript):
    """
    Extract important keywords from the transcript.
    """

    if not transcript:
        return []

    if transcript.startswith("Transcript not available"):
        return []

    transcript = transcript[:12000]

    prompt = f"""
You are an AI assistant.

Extract the 10 most important keywords from the following YouTube transcript.

Rules:
- Return ONLY the keywords.
- One keyword per line.
- Do not number them.
- Do not add explanations.

Transcript:

{transcript}
"""

    try:

        response = model.generate_content(prompt)

        keywords = []

        for line in response.text.split("\n"):

            line = line.strip()

            if line:
                keywords.append(line)

        return keywords

    except Exception:

        return []