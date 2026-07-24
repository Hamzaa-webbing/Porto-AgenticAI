# **Smart Market Intelligence Agent**:

An AI-powered Market Intelligence Agent that automatically scrapes web content and generates actionable business insights via Telegram Bot.

1. Key Features:
    - Automated Web Data Extraction: Scrapes text content from target URLs using BeautifulSoup.
    - AI-Powered Analysis: Utilizes Google Gemini API with tailored prompt engineering to summarize, extract business insights, and suggest actionable recommendations.
    - Interactive Telegram Bot: Accessible via Telegram for real-time analysis on the go.
    - Modular Architecture: Clean separation between scraper logic, AI orchestration, and bot interface.

2. Architecture Flow:
    `User Link (Telegram)` ➔ `Scraper (BeautifulSoup)` ➔ `AI Agent (Gemini API)` ➔ `Structured Analysis Report`

3. Tech Stack:
    - Language: Python 3.11+
    - AI Model: Google Gemini API (`google-genai`)
    - Scraping: BeautifulSoup4, Requests
    - Bot Framework: `python-telegram-bot`
    - Environment: `python-dotenv`


## **How to Run Locally**:

1. Clone Repository
   '''bash:
   git clone [https://github.com/Hamzaa_webbing/Porto-AgenticAI/01-smart-market-agent.git](https://github.com/Hamzaa_webbing/Porto-AgenticAI/01-smart-market-agent.git)
   cd 01-smart-market-agent

2. Setup virtual environment:
    - python -m venv venv
    - source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    - pip install -r requirements.txt

3. Config Environment Variable:
    GEMINI_API_KEY=your_gemini_api_key
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token


