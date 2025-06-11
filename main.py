import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("TOKEN")

# Словарь товаров по категориям с ценами
PRODUCTS = {
    "Пельмени": [
        ("Пельмени со свининой-говядиной", "1150 дин/kg"),
        ("Пельмени с говядиной", "1300 дин/kg"),
        ("Пельмени с курицей", "1000 дин/kg")
    ],
    "Вареники": [
        ("Вареники с картофелем и луком", "750 дин/kg"),
        ("Вареники с картофелем и шампиньонами", "1000 дин/kg"),
        ("Вареники с творогом", "1150 дин/kg"),
        ("Вареники с вишней", "1100 дин/kg")
    ],
    "Сырники и блинчики": [
        ("Сырники", "800 дин/10 штук"),
        ("Блинчики с яблоком и корицей", "600 дин/500гр"),
        ("Блинчики с творогом", "600 дин/500гр")
        ("Блины с курицей", "750 дин/500гр"),
        ("Блины с мясом", "750 дин/500гр")      
    ],
    "Тортики": [
        ("Медовик", "440 дин/160гр"),
        ("Медовик", "4190 дин/1.7кг"),
        ("Красный бархат", "490 дин/160гр"),
        ("Медовик", "4890 дин/1.7кг"),
    ]
}

# Старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"🥟Привет, {user.first_name}! Baikal - эта те самые пельмени ручной лепки из Белграда. Только натуральный состав и никаких добавок! \n\nДоставку осуществляем с понедельника по среду в период с 19:00 до 23:00. Для заказа добавьте в корзину товары из категорий ниже:",
        reply_markup=ReplyKeyboardMarkup([
            ["Пельмени", "Вареники"],
            ["Сырники и блинчики", "Тортики"],
            ["Ваша корзина"]
        ], resize_keyboard=True)
    )

# Обработка текста
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text in PRODUCTS:
        # Формируем список товаров с ценами в виде текста
        product_list = "\n".join([f"- {name} — {price}" for name, price in PRODUCTS[text]])
        await update.message.reply_text(f"Вы выбрали: {text}.\nВот наши товары:\n{product_list}")
    elif text == "Ваша корзина":
        # Пока заглушка
        await update.message.reply_text("Ваша корзина пуста")
    else:
        await update.message.reply_text("Пожалуйста, выберите категорию из меню")

# Запуск
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
