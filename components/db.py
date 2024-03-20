import sqlite3

from settings.prod import DB

CREATE_DB_QUERY = """CREATE TABLE IF NOT EXISTS birthdays
                    (id INTEGER PRIMARY KEY,
                    chat_id INTEGER,
                    name TEXT,
                    relative TEXT,
                    birthdate DATE,
                    interests TEXT,
                    wishes TEXT)"""


def create_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(CREATE_DB_QUERY)
    conn.commit()
    conn.close()