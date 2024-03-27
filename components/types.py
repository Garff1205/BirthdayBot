from typing import TypedDict


class Person(TypedDict):
    chat_id: int
    name: str
    relationship: str
    birthdate: str
    interests: str
    wishes: str
