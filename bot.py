from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN="8746235673:AAEIf0rUGBdSsxtrGLj9J-h2M8Wtg5_FoN4"

keyboard = [
    ["درباره ما", "تماس با ما"],
    ["سفارش"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\nبه ربات خوش اومدی.\nیکی از گزینه‌ها رو انتخاب کن:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "درباره ما":
        await update.message.reply_text("ما یک فروشگاه/مجموعه خدماتی هستیم و خوشحالیم که کنار شما هستیم 🌷")

    elif text == "تماس با ما":
        await update.message.reply_text("شماره تماس: 0912xxxxxxx\nآیدی پشتیبانی: @yourid")

    elif text == "سفارش":
        await update.message.reply_text("برای ثبت سفارش، لطفاً نام محصول یا درخواستت رو برام بفرست ✍️")

    else:
        await update.message.reply_text(f"پیامت دریافت شد:\n{text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات روشن شد...")
    app.run_polling()

if __name__ == "__main__":
    main()
