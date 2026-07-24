import requests
from bs4 import BeautifulSoup

def scrape_website_text(url: str) -> str:
    """
    Fungsi untuk mengambil teks utama dari sebuah halaman web.
    """

    # header agar request kita tidak diblokir oleh sistem anti-bot sederhana
    headers = {
        "User-Agent": "Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # cek apakah HTTP status 200 (berarti ok)

        # parsing HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # hapus tag yang tidak berisi konten utama (script, style, nav, footer)
        for element in soup(["script", "style", "header", "footer", "nav"]):
            element.extract()

        # ambil semua paragraf <p>
        paragraphs = soup.find_all('p')
        text_content = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])

        # batasi panjang teks agar tidak over token, misal 3000 karakter
        return text_content[:3000] if text_content else "Tidak ditemukan teks paragraf pada URL ini"

    except Exception as e:
        return f"Error scraping URL: {e}"

# Test skrip scraper
if __name__ == "__main__":
        print("🌐 Testing Web Scraper")
        # coba scraper artikel tren sederhana
        test_url = "https://id.wikipedia.org/wiki/Pemasaran_digital"

        hasil_scraping = scrape_website_text(test_url)
        print(f"\nHasil Scraping (500 karakter pertama):\n" + "-"*40)
        print(hasil_scraping[:500] + "...\n")