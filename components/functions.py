from telegram import Bot

from components.db import db_get_today_birthdays
from components.helpers import get_wish


async def create_birthday_wish(bot: Bot) -> None:
    today_birthdays = db_get_today_birthdays()

    birth_dict = {}
    # fill the dictionary key - chat_id, value - list of birthday people
    for person in today_birthdays:
        if person[0] in birth_dict:
            birth_dict[person[0]].append(person)
        else:
            birth_dict[person[0]] = [person]

    for chat_id, people in birth_dict.items():

        await bot.send_message(chat_id=chat_id, text="Поздравления для сегодняшних именинников!")

        for person in people:
            await bot.send_message(chat_id=chat_id, text=f"{person[1]}: \n {get_wish(person)}")
