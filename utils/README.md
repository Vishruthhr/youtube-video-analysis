# YouTube Video Analysis System

## Overview

This project analyzes public YouTube videos using Artificial Intelligence.

## Features

- Video metadata extraction
- Transcript extraction
- AI-generated summary
- Sentiment analysis
- Keyword extraction
- Topic detection
- AI question answering
- PDF report generation
- Analysis history using SQLite
- Local fallback analysis when AI is unavailable

## Technologies Used

- Python
- Flask
- Google Gemini API
- yt-dlp
- youtube-transcript-api
- ReportLab
- SQLite
- Bootstrap 5

## Installation

```bash
git clone <repository-url>

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
├── README.md
├── history.db
├── utils/
├── templates/
├── static/
```

## Screenshots

(Add screenshots here after uploading to GitHub.)

## Author

Vishruth HR