# 🎥 AI-Powered YouTube Video Analysis System

An AI-powered web application that analyzes YouTube videos using Flask and Google Gemini AI.

## Features

- 📺 Analyze any public YouTube video
- 📝 Automatic transcript extraction
- 🤖 AI-generated summary
- 😊 Sentiment analysis
- 🔑 Keyword extraction
- 🏷 Topic detection
- 💬 Ask questions about the video
- 📄 Generate downloadable PDF reports
- 📚 Analysis history with SQLite database

## Technologies Used

- Python
- Flask
- Google Gemini API
- yt-dlp
- YouTube Transcript API
- SQLite
- Bootstrap 5
- ReportLab

## Installation

```bash
git clone https://github.com/Vishruthhr/youtube-video-analysis.git
cd youtube-video-analysis

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Project Structure

```
youtube-video-analysis/
│
├── app.py
├── config.py
├── requirements.txt
├── static/
├── templates/
├── utils/
└── reports/
```

## Author

**Vishruth HR**
