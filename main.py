from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram.ext import Application, CommandHandler

from components.commands import start, add_birthday, check_all_birthdays
from components.functions import create_birthday_wish
from settings.prod import TOKEN


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        func=create_birthday_wish,
        trigger="cron",
        hour=13,
        minute=0,
        kwargs={"bot": application.bot},
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_birthday))
    application.add_handler(CommandHandler("check", check_all_birthdays))

    scheduler.start()
    application.run_polling()


if __name__ == "__main__":
    main()
