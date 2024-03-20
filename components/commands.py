from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

from components.db import db_add_birthday, db_get_all_birthdays


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я бот который напомнит тебе про др твоих близких, друзей и всех кого ты хочешь не забыть. "
        "А так же сразу придумает для тебя поздравление! Для добавления нового человека используй команду /add."
    )


async def add_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = " ".join(context.args).split("; ")
    if len(args) == 5:
        db_add_birthday(update.message.chat_id, *args)
    else:
        await update.message.reply_text(
            "Пожалуйста, используйте формат: "
            "/add <имя именинника>; "
            "<ваши с ним отношения (друг, сестра, дальний родственник>; "
            "<дата рождения в формате YYYY-MM-DD>; "
            "<интересы именника>; "
            "<дополнительные пожелания к тексту поздравления>"
        )


async def check_all_birthdays(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    people = db_get_all_birthdays(update.message.chat_id)
    message_text = "\n".join([f"Имя: {person[0]}, дата рождения: {datetime.strptime(person[2], '%Y-%m-%d').strptime('%d %B %Y')}" for person in people])
    await update.message.reply_text(message_text)
