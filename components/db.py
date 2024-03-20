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

ADD_BIRTHDAY_QUERY = """INSERT INTO birthdays (chat_id, name, relative, birthdate, interests, wishes) VALUES (?, ?, ?, ?, ?, ?)"""


def create_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(CREATE_DB_QUERY)
    conn.commit()
    conn.close()


def db_add_birthday(chat_id, name, relative, birthdate, interests, wishes):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(ADD_BIRTHDAY_QUERY, (chat_id, name, relative, birthdate, interests, wishes))
    conn.commit()
    conn.close()
