import sqlite3

DB_NAME = "history.db"


def init_db():
    """
    Create the history table if it doesn't exist.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            video_id TEXT UNIQUE,

            title TEXT,

            channel TEXT,

            url TEXT,

            summary TEXT,

            sentiment TEXT,

            topic TEXT,

            analyzed_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


def save_history(title, channel, url):
    """
    Save a video analysis to history.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history
        (
            title,
            channel,
            url
        )
        VALUES(?,?,?)
    """, (
        title,
        channel,
        url
    ))

    conn.commit()
    conn.close()


def get_history():
    """
    Return all history records.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            channel,
            analyzed_on,
            url
        FROM history
        ORDER BY analyzed_on DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_history(history_id):
    """
    Delete a history record by ID.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM history WHERE id=?",
        (history_id,)
    )

    conn.commit()
    conn.close()