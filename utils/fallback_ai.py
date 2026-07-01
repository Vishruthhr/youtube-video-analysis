import re
from collections import Counter


STOPWORDS = {
    "the", "and", "for", "that", "this", "with", "you", "your",
    "from", "have", "will", "they", "their", "there", "about",
    "what", "when", "where", "which", "would", "could", "should",
    "into", "been", "being", "are", "was", "were", "them", "then",
    "than", "also", "just", "very", "more", "some", "each", "only",
    "because", "while", "using", "used", "like", "into", "here",
    "going", "know", "want", "over", "click", "version", "make",
    "makes", "made", "time", "people", "course", "video", "today",
    "really", "much", "well", "need", "start", "getting", "learn",
    "learning", "teach", "teaching", "thing", "things", "look",
    "looked", "looking", "actually", "okay", "first", "next"
}


TOPIC_KEYWORDS = {
    "Python": [
        "python",
        "pycharm",
        "django",
        "flask",
        "numpy",
        "pandas",
        "variable",
        "function",
        "loop",
        "class"
    ],
    "Machine Learning": [
        "machine",
        "learning",
        "model",
        "dataset",
        "training",
        "tensorflow",
        "keras",
        "neural"
    ],
    "Web Development": [
        "html",
        "css",
        "javascript",
        "react",
        "bootstrap",
        "web",
        "frontend",
        "backend"
    ],
    "Blockchain": [
        "blockchain",
        "ethereum",
        "smart",
        "contract",
        "web3",
        "crypto"
    ]
}


def detect_topic(text):

    lower = text.lower()

    for topic, words in TOPIC_KEYWORDS.items():

        for word in words:

            if word in lower:
                return topic

    return "General"


def fallback_analysis(transcript):

    if not transcript.strip():

        return {
            "summary": "Transcript unavailable.",
            "sentiment": "Unknown",
            "confidence": "0%",
            "reason": "Transcript unavailable.",
            "keywords": [],
            "topic": "Unknown"
        }

    words = transcript.split()

    summary = " ".join(words[:180])

    tokens = re.findall(r"[A-Za-z]{4,}", transcript.lower())

    filtered = [
        word
        for word in tokens
        if word not in STOPWORDS
    ]

    counts = Counter(filtered)

    keywords = [
        word.title()
        for word, _ in counts.most_common(10)
    ]

    lower = transcript.lower()

    positive = [
        "good",
        "excellent",
        "best",
        "easy",
        "powerful",
        "success"
    ]

    negative = [
        "error",
        "bad",
        "problem",
        "issue",
        "fail",
        "warning"
    ]

    pos = sum(lower.count(word) for word in positive)
    neg = sum(lower.count(word) for word in negative)

    if pos > neg:

        sentiment = "Positive"
        confidence = "78%"

    elif neg > pos:

        sentiment = "Negative"
        confidence = "72%"

    else:

        sentiment = "Neutral"
        confidence = "65%"

    return {

        "summary": summary + "...",

        "sentiment": sentiment,

        "confidence": confidence,

        "reason": "Generated using local AI fallback.",

        "keywords": keywords,

        "topic": detect_topic(transcript)

    }