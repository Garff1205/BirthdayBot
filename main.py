from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram.ext import Application, CommandHandler

from components.commands import handlers
from components.functions import send_all_today_birthday_wishes
from settings.prod import TOKEN, DEBUG


def main() -> None:
    # Init bot
    application = Application.builder().token(TOKEN).build()

    # Init scheduler and add daily job for birthday wishes sent
    scheduler = AsyncIOScheduler()
    scheduler_job_args = {
        'func': send_all_today_birthday_wishes,
        'trigger': "cron",
        'kwargs': {"bot": application.bot}
    }
    scheduler_job_timing = {'second': 0} if "TIME" in DEBUG else {'hour': 13, 'minute': 0}
    scheduler.add_job(**scheduler_job_timing, **scheduler_job_args)

    # Add handlers to the bot
    for item in handlers.items():
        application.add_handler(CommandHandler(*item))

    # Start the bot and scheduler
    scheduler.start()
    application.run_polling()


if __name__ == "__main__":
    main()
