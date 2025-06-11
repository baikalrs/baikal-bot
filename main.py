
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

logging.basicConfig(level=logging.INFO)
TOKEN = "8132011800:AAGm9Me8jfaETGByekhK4MQe99ESDR47two"

# Старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! Добро пожаловать в Baikal 🥟.\n\nВыбери категорию товара:",
        reply_markup=ReplyKeyboardMarkup([
            ["Пельмени", "Вареники"],
            ["Сырники и блинчики", "Тортики"],
            ["Ваша корзина"]
        ], resize_keyboard=True)
    )

# Обработка текста
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Вы выбрали: {text}. (Здесь будет выбор товаров).")

# Запуск
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
