import os
import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Environment Variables ---
WEB_APP_URL = os.environ.get("WEB_URL")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command.
    Greets the user and provides a button to register/login via the web app.
    """
    user = update.effective_user
    logger.info(f"User {user.id} ({user.first_name}) started the bot.")

    text = (
        f"Selamat datang, {user.first_name}!\n\n"
        "Ini adalah Panel Hosting Bot. Untuk mendaftar atau masuk ke dashboard Anda, "
        "silakan tekan tombol di bawah ini."
    )

    # The WebAppInfo object points to the web app that will handle the login.
    # The web app will receive user data from Telegram upon authorization.
    keyboard = [
        [
            InlineKeyboardButton(
                "Buka Dashboard",
                web_app=WebAppInfo(url=f"{WEB_APP_URL}?start_param=from_bot")
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_html(text, reply_markup=reply_markup)


async def not_implemented(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Placeholder for commands that are not yet implemented.
    """
    await update.message.reply_text("Fitur ini sedang dalam pengembangan.")
