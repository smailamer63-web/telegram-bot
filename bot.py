import telebot
import os
from auth import create_user, generate_token

TOKEN = os.getenv("8382890875:AAHCA9vHKtwlpRHq45mNVfQ3XATI5m-2lLg")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = {
        "telegram_id": message.from_user.id,
        "name": message.from_user.first_name
    }

    create_user(user)
    token = generate_token(user["telegram_id"])

    miniapp_url = f"https://smailamer63-web.github.io/telegram-miniapp2/?token={token}"

    bot.send_message(
        message.chat.id,
        f"👋 مرحبًا {user['name']}\n\n"
        f"🚀 افتح حسابك:\n{miniapp_url}"
    )

bot.infinity_polling()
