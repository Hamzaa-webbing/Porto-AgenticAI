from scraper import scrape_website_text
from agent import analyze_scraped_data

def main():
    print("==========================================")
    print("🤖 SMART MARKET INTELLIGENCE AGENT (CLI) 🤖")
    print("==========================================\n")

    # minta URL yang mau dianalisis dari user
    target_url = input("Masukkan URL website/artikel yang mau dianalisis").strip()

    if not target_url:
        print("❌ URL tidak boleh kosong!")
        return

    print(f"\n⏳ [1/2] Sedang mengunduh dan membaca konten dari: {target_url}...")
    raw_text = scrape_website_text(target_url)

    # cek jika scraping gagal
    if raw_text.startswith("Error") or raw_text.startswith("Tidak ditemukan"):
        print(f"❌ Scraping gagal: {raw_text}")
        return

    print("✅ Berhasil mengambil data!")
    print("\n ⏳ [2/2] AI Agent sedang menganalisis data ...\n")

    # kirim data hasil scraping ke AI Agent
    analysis_result = analyze_scraped_data(target_url, raw_text)

    # tampilkan hasil analisis
    print("="*50)
    print("📊 LAPORAN ANALISIS MARKET INTELLIGENCE")
    print("="*50)
    print(analysis_result)
    print("="*50)

if __name__ == "__main__":
    main()