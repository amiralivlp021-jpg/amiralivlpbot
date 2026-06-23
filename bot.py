import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8746235673:AAEIf0rUGBdSsxtrGLj9J-h2M8Wtg5_FoN4"

keyboard = [
    ["درباره ما", "تماس با ما"],
    ["سفارش"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "به ربات خوش اومدی.\n"
        "یکی از گزینه‌های زیر را انتخاب کن:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "درباره ما":
        await update.message.reply_text(
            "🌹 درباره ما\n\n"
            "ما یک مجموعه خدماتی هستیم و آماده ارائه خدمات به شما هستیم."
        )

    elif text == "تماس با ما":
        await update.message.reply_text(
            "📞 شماره تماس: 0912XXXXXXX\n"
            "🆔 تلگرام: @yourid"
        )

    elif text == "سفارش":
        await update.message.reply_text(
            "📝 لطفاً سفارش یا درخواست خود را ارسال کنید."
        )

    else:
        await update.message.reply_text(
            f"✅ پیام شما دریافت شد:\n\n{text}"
        )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("ربات روشن شد...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
