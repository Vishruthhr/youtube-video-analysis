import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def local_answer(transcript, question):
    """
    Simple fallback when Gemini is unavailable.
    """

    if not transcript:
        return "Transcript not available."

    question = question.lower()

    sentences = transcript.split(".")

    keywords = [
        word
        for word in question.split()
        if len(word) > 3
    ]

    for sentence in sentences:

        sentence_lower = sentence.lower()

        for keyword in keywords:

            if keyword in sentence_lower:
                return sentence.strip()

    return (
        "Gemini API is currently unavailable. "
        "I couldn't confidently answer your question from the transcript."
    )


def ask_question(transcript, question):
    """
    Answer user's question using Gemini.
    Falls back to local search if Gemini fails.
    """

    if not transcript or not transcript.strip():
        return "Transcript not available."

    prompt = f"""
You are an AI assistant.

Answer ONLY from the transcript below.

If the answer is not present,
reply exactly:

"I couldn't find that information in the video."

Transcript:
{transcript}

Question:
{question}

Answer:
"""

    try:

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception:

        # Local fallback instead of showing Gemini errors
        return local_answer(transcript, question)