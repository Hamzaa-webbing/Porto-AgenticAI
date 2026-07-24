import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import modul yang sudah dibuat
from scraper import scrape_website_text
from agent import analyze_scraped_data

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# konfig logging untuk pemantau error
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Command /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text= (
        "🤖 Selamat datang di Smart Market Intelligence Agent!\n\n"
        "Kirimkan link/URL artikel atau website bisnis yang ingin kamu analisis. "
        "Saya akan membaca websitenya dan memberikan laporan analisis pasar secara otomatis! 📊"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    target_url = update.message.text.strip()

    # validasi sederhana apakah input berupa URL
    if not target_url.startswith(("http://", "https://")):
        await update.message.reply_text("❌ Kirimkan URL yang valid (diawali http:// atau https://).")
        return

    # kirim status awal ke user
    status_msg = await update.message.reply_text(f"[1/2] Sedang membaca konten dari: {target_url} ....")

    # scraping data
    raw_text = scrape_website_text(target_url)

    if raw_text.startswith("Error") or raw_text.startswith("Tidak ditemukan"):
        await status_msg.edit_text(f"❌ Scraping gagal: {raw_text}")
        return

    # update status ke user
    await status_msg.edit_text("✅ Berhasil membaca data!\n⏳ [2/2] AI Agent sedang menganalisis pasar...")

    # analisis dengan agent AI
    analysis_result = analyze_scraped_data(target_url, raw_text)

    # kirim hasil alasis akhir
    await status_msg.edit_text(f"📊 LAPORAN ANALISIS MARKET INTELLIGENCE \n\n{analysis_result}", parse_mode="Markdown")

def main():
    if not TELEGRAM_TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN belum diset di file .env!")
        return

    print("🚀 Bot Telegram sedang berjalan...")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # register handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # jalankan bot
    app.run_polling()

if __name__ == "__main__":
    main()