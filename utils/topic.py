import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def detect_topic(transcript):

    if not transcript:
        return "Unknown"

    transcript = transcript[:10000]

    prompt = f"""
Identify the main topic/category of this YouTube video.

Return ONLY one category.

Examples:
Education
Technology
Gaming
Music
Finance
Health
Sports
News
Comedy
Food
Travel
Science
Programming
Business
Motivation

Transcript:

{transcript}
"""

    try:

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception:

        return "Unknown"