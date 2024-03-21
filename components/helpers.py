from components.db import db_get_today_birthdays
from openai import OpenAI

from settings.prod import DEBUG


def get_wishes():
    persons = db_get_today_birthdays()

    text = ""
    for person in persons:
        text += f"имя - {person[1]}; отношения - {person[2]}; интересы - {person[4]}; пожелания - {person[5]};\n"

    if not DEBUG:

        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """
                 Сгенерируйте поздравления с днем рождения для нескольких людей, учитывая их имена, отношения 
                 поздравляющего и именинника, интересы и специфические пожелания. Каждое поздравление должно быть кратким, 
                 в пределах 1-3 предложений. Поздравления должны быть разделены двойным символом ";;". Пожалуйста, 
                 учитывайте эти детали при составлении поздравлений.
                 """,
                },
                {
                    "role": "user",
                    "content": f"список людей для поздравления: \n {text}",
                },
            ],
        )

        response = completion.choices[0].message.content

    else:
        wishes = []
        for person in persons:
            wishes.append(f"Сгенерированное поздравление для {person[1]}")

        response = ";;".join(wishes)

    return [
        {"chat_id": person[0], "name": person[1], "wish": wish}
        for person, wish in zip(persons, response.split(";;"))
    ]
