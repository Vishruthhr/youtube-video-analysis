import json
import google.generativeai as genai

from config import GEMINI_API_KEY
from utils.fallback_ai import fallback_analysis

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_video(transcript):
    """
    Analyze the transcript using Gemini.
    If Gemini fails (quota/network/etc.), use the local fallback analyzer.
    """

    if not transcript:
        return {
            "summary": "Transcript not available.",
            "sentiment": "Unknown",
            "confidence": "0%",
            "reason": "Transcript unavailable.",
            "keywords": [],
            "topic": "Unknown"
        }

    # Limit transcript length to reduce token usage
    transcript = transcript[:12000]

    prompt = f"""
Analyze the following YouTube transcript.

Return ONLY valid JSON in this exact format:

{{
    "summary": "...",
    "sentiment": "Positive",
    "confidence": "95%",
    "reason": "...",
    "keywords": [
        "Python",
        "Programming",
        "Variables",
        "Functions",
        "Loops"
    ],
    "topic": "Programming"
}}

Transcript:
{transcript}
"""

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove Markdown code fences if Gemini returns them
        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        return json.loads(text)

    except Exception:
        # Use local analysis if Gemini fails
        return fallback_analysis(transcript)