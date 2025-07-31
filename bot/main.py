import os
import logging
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

from handlers import start, not_implemented

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Environment Variables ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Tidak ada BOT_TOKEN yang ditemukan di environment variables")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("list", not_implemented))
    application.add_handler(CommandHandler("stop", not_implemented))
    application.add_handler(CommandHandler("restart", not_implemented))
    application.add_handler(CommandHandler("delete", not_implemented))
    application.add_handler(CommandHandler("logs", not_implemented))

    # Run the bot until the user presses Ctrl-C
    logger.info("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
