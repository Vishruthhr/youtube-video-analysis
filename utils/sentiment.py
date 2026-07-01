import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_sentiment(transcript):
    """
    Analyze the sentiment of a YouTube transcript.
    """

    if not transcript:
        return {
            "sentiment": "Unknown",
            "confidence": "0%",
            "reason": "Transcript not available."
        }

    transcript = transcript[:12000]

    prompt = f"""
Analyze the following YouTube transcript.

Return ONLY in this format:

Sentiment: Positive/Neutral/Negative
Confidence: XX%
Reason: one short sentence

Transcript:

{transcript}
"""

    try:
        response = model.generate_content(prompt)

        lines = response.text.strip().split("\n")

        sentiment = "Unknown"
        confidence = "0%"
        reason = "No reason available."

        for line in lines:

            if line.lower().startswith("sentiment"):
                sentiment = line.split(":", 1)[1].strip()

            elif line.lower().startswith("confidence"):
                confidence = line.split(":", 1)[1].strip()

            elif line.lower().startswith("reason"):
                reason = line.split(":", 1)[1].strip()

        return {
            "sentiment": sentiment,
            "confidence": confidence,
            "reason": reason
        }

    except Exception as e:

        return {
            "sentiment": "Error",
            "confidence": "0%",
            "reason": str(e)
        }