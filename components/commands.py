from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я бот который напомнит тебе про др твоих близких, друзей и всех кого ты хочешь не забыть. "
        "А так же сразу придумает для тебя поздравление! Для добавления нового человека используй команду /add."
    )


async def add_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def check_all_birthdays(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
