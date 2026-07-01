from flask import (
    Flask,
    render_template,
    request,
    send_file,
    redirect,
    url_for
)

import os

from utils.youtube import get_video_info
from utils.transcript import get_transcript
from utils.ai_analyzer import analyze_video
from utils.qa import ask_question
from utils.pdf_report import create_pdf_report
from utils.database import (
    init_db,
    save_history,
    get_history,
    delete_history
)

app = Flask(__name__)

# Initialize database
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    video_url = request.form.get("video_url", "").strip()
    question = request.form.get("question", "").strip()
    download_pdf = request.form.get("download_pdf")

    if not video_url:
        return render_template(
            "index.html",
            error="Please enter a YouTube URL."
        )

    # -----------------------
    # Video Information
    # -----------------------

    video = get_video_info(video_url)

    if "error" in video:

        return render_template(
            "result.html",
            video=video,
            transcript="",
            summary="",
            sentiment={},
            keywords=[],
            topic="Unknown",
            question="",
            answer=""
        )

    # -----------------------
    # Transcript
    # -----------------------

    transcript = get_transcript(video_url)

    # -----------------------
    # AI Analysis
    # -----------------------

    analysis = analyze_video(transcript)

    summary = analysis.get("summary", "")

    sentiment = {
        "sentiment": analysis.get("sentiment", "Unknown"),
        "confidence": analysis.get("confidence", "0%"),
        "reason": analysis.get("reason", "")
    }

    keywords = analysis.get("keywords", [])

    topic = analysis.get("topic", "Unknown")

    # -----------------------
    # Question Answering
    # -----------------------

    answer = ""

    if question:

        answer = ask_question(
            transcript,
            question
        )

    # -----------------------
    # Save History
    # -----------------------

    try:

        save_history(
            video["title"],
            video["channel"],
            video_url
        )

    except Exception:

        pass

    # -----------------------
    # Download PDF
    # -----------------------

    if download_pdf == "true":

        os.makedirs(
            "reports",
            exist_ok=True
        )

        pdf_path = os.path.join(
            "reports",
            "YouTube_Analysis_Report.pdf"
        )

        create_pdf_report(
            filename=pdf_path,
            video=video,
            summary=summary,
            sentiment=sentiment,
            keywords=keywords,
            topic=topic,
            question=question,
            answer=answer
        )

        return send_file(
            pdf_path,
            as_attachment=True
        )

    # -----------------------
    # Dashboard
    # -----------------------

    return render_template(
        "result.html",
        video=video,
        transcript=transcript,
        summary=summary,
        sentiment=sentiment,
        keywords=keywords,
        topic=topic,
        question=question,
        answer=answer
    )


@app.route("/history")
def history():

    history_data = get_history()

    return render_template(
        "history.html",
        history=history_data
    )


@app.route("/delete/<int:history_id>")
def delete(history_id):

    delete_history(history_id)

    return redirect(
        url_for("history")
    )


@app.errorhandler(404)
def page_not_found(e):

    return render_template(
        "404.html"
    ), 404


if __name__ == "__main__":
    app.run(debug=True)