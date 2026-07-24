import os
from dotenv import load_dotenv
from google import genai

# muat environment variable dari file .env
load_dotenv()

# ambil API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY tidak ditemukan! Pastikan sudah diisi di file .env")

# inisialisai gemini client
client = genai.Client(api_key=api_key)

def ask_market_agent(prompt: str) -> str:
    """
    Fungsi dasar untuk mengirimkan prompt ke model AI Gemini.
    """

    # system instruction untuk membentuk persona Agent
    system_instruction = (
        "Kamu adalah seorang Market Intelligence Analyst profesional. "
        "Tugasmu adalah menganalisis tren pasar, strategi kompetitor, dan "
        "memberikan insigt bisnis yang tajam, ringkas, serta actionable."
    )

    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash-lite',
            contents=prompt,
            config={
                'system_instruction': system_instruction,
                'temperature': 0.7,
            }
        )
        return response.text
    except Exception as e:
        return f"❌ Error saat memanggil API: {e}"

def analyze_scraped_data(url: str, text_content: str) -> str:
    """
    Fungsi khusus untuk menganalisis data hasil scraping web.
    """
    prompt = f"""
    Berikut adalah teks yang berhasil ditarik dari URL: {url}

    --- AWAL KONTEN ---
    {text_content}
    --- AKHIR KONTEN ---

    Berdasarkan data di atas, berikan laporan analisis singkat dengan format:
    1. 📌 **Ringkasan Utama** (2-3 kalimat)
    2. 💡 **Peluang / Insight Bisnis** (Bullet points)
    3. 🎯 **Rekomendasi Aksi** (Langkah konkret yang bisa diambil)
    """

    # menggunakan fungsi dasar ask_market_agent yang sudah dibuat sebelumnya
    return ask_market_agent(prompt)
    
    

# TEST SKRIP
if __name__ == "__main__":
        print("🤖 Agent Market Intelligence Siap!")
        test_query = "Berikan 3 tren bisnis digital terpanas saat ini secara ringkas."

        print(f"\nPertanyaan: {test_query}\n" + "-"*40)
        jawaban = ask_market_agent(test_query)
        print(f"Jawaban Agent:\n{jawaban}")