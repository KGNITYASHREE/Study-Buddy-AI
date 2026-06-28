import sqlite3


def create_database():

    conn = sqlite3.connect("student.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        subject TEXT,
        goal TEXT,
        weak_topic TEXT
    )
    """)

    conn.commit()
    conn.close()



def save_student(name, subject, goal, weak_topic):

    conn = sqlite3.connect("student.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (name, subject, goal, weak_topic)
        VALUES (?, ?, ?, ?)
        """,
        (name, subject, goal, weak_topic)
    )

    conn.commit()
    conn.close()



def save_progress(subject, topic, score):

    conn = sqlite3.connect("student.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress(
        id INTEGER PRIMARY KEY,
        subject TEXT,
        topic TEXT,
        score INTEGER
    )
    """)

    cursor.execute(
        """
        INSERT INTO progress
        (subject, topic, score)
        VALUES (?, ?, ?)
        """,
        (subject, topic, score)
    )

    conn.commit()
    conn.close()