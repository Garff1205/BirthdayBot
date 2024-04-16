from typing import List, Dict

from components.db import db_get_today_birthdays
from openai import OpenAI

from settings.prod import DEBUG
from components.types import Person


def get_wishes(persons: List[Person] = None) -> List[Dict[str, str]]:
    persons: List[Person] = persons or db_get_today_birthdays()

    text = ""
    for person in persons:
        text += (f"имя - {person['name']}; отношения - {person['relationship']}; интересы - {person['interests']}; "
                 f"пожелания - {person['wishes']};\n")

    if "GPT" in DEBUG:
        wishes = []
        for person in persons:
            wishes.append(f"Сгенерированное поздравление для {person['name']}")

        response = ";;".join(wishes)
    else:
        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """
                         Сгенерируйте поздравления с днем рождения для нескольких людей, учитывая их имена, отношения 
                         поздравляющего и именинника, интересы и специфические пожелания. Каждое поздравление должно 
                         быть кратким, в пределах 1-3 предложений. Поздравления должны быть разделены двойным символом 
                         ";;". Пожалуйста, учитывайте эти детали при составлении поздравлений.
                         """,
                },
                {
                    "role": "user",
                    "content": f"список людей для поздравления: \n {text}",
                },
            ],
        )

        response = completion.choices[0].message.content

    return [
        {"chat_id": person["chat_id"], "name": person["name"], "wish": wish}
        for person, wish in zip(persons, response.split(";;"))
    ]
