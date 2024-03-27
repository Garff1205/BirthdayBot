import sqlite3
from typing import List

from components.types import Person
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

GET_ALL_BIRTHDAYS_QUERY = """SELECT name, relative, birthdate, interests, wishes FROM birthdays WHERE chat_id = ?"""

GET_TODAY_BIRTHDAYS_QUERY = """SELECT chat_id, name, relative, birthdate, interests, wishes FROM birthdays WHERE strftime('%m-%d', birthdate) = strftime('%m-%d', 'now')"""


def create_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(CREATE_DB_QUERY)
    conn.commit()
    conn.close()


def db_add_birthday(chat_id, name, relative, birthdate, interests, wishes):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        ADD_BIRTHDAY_QUERY, (chat_id, name, relative, birthdate, interests, wishes)
    )
    conn.commit()
    conn.close()


def db_get_all_birthdays(chat_id: int) -> List[Person]:
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(GET_ALL_BIRTHDAYS_QUERY, (chat_id, ))
    birthdays = c.fetchall()
    conn.close()
    return [
        {
            "chat_id": chat_id,
            "name": birthday[1],
            "relationship": birthday[2],
            "birthdate": birthday[3],
            "interests": birthday[4],
            "wishes": birthday[5],
        }
        for birthday in birthdays
    ]


def db_get_today_birthdays() -> List[Person]:
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(GET_TODAY_BIRTHDAYS_QUERY)
    birthdays = c.fetchall()
    conn.close()
    return [
        {
            "chat_id": birthday[0],
            "name": birthday[1],
            "relationship": birthday[2],
            "birthdate": birthday[3],
            "interests": birthday[4],
            "wishes": birthday[5],
        }
        for birthday in birthdays
    ]


if __name__ == "__main__":
    create_db()
