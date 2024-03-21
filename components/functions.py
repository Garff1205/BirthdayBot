from telegram import Bot

from components.helpers import get_wishes


async def create_birthday_wish(bot: Bot) -> None:
    wishes = get_wishes()

    messages_by_chat_id = {}
    for element in wishes:
        message = f"Поздравление для {element['name']}: \n\n {element['wish']}"
        if element["chat_id"] in messages_by_chat_id:
            messages_by_chat_id[element["chat_id"]].append(message)
        else:
            messages_by_chat_id[element["chat_id"]] = [message]

    for chat_id, messages in messages_by_chat_id.items():
        await bot.send_message(chat_id=chat_id, text="\n\n".join(messages))
