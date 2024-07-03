import telebot
from config import Config

bot = telebot.TeleBot(Config.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    webapp_url = 'https://your-webapp-url.com'  # Замените на URL вашего веб-приложения
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("Start Game", web_app=telebot.types.WebAppInfo(webapp_url))
    markup.add(btn)
    bot.send_message(message.chat.id, "Welcome to Ramble Coin!", reply_markup=markup)

bot.polling()
