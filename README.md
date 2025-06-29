# LangChain-Email-Newsletter-Writer
This project is an **automated email newsletter generator** written in Python.  
It fetches content from RSS feeds, adjusts the tone and length, and creates a clean HTML newsletter.

---

## ✨ Features

✅ **Content Curation**
- RSS Feed integration (e.g., TechCrunch)
- Optional web scraping example

✅ **Newsletter Generation**
- Clean, professional HTML output
- Summaries trimmed and tone-adjusted
- Call-to-action button included

✅ **Personalization**
- Basic subscriber preferences:
  - Preferred topics
  - Tone (friendly/formal)
  - Length (short/full)

---

## 🛠️ Requirements

- Python **3.8+**
- Dependencies:

  ```bash
  pip install feedparser beautifulsoup4 jinja2 requests

🚀 How to Use

    Clone this repository:

git clone https://github.com/monu20050608/langchain-newsletter-writer.git
cd langchain-newsletter-writer

Install dependencies:

pip install feedparser beautifulsoup4 jinja2 requests

Run the script:

python main.py

Open newsletter.html:

    Windows:

        start newsletter.html

        Or manually double-click in File Explorer.

# 📝 Project Structure

.
├── main.py              # Main script
├── newsletter.html      # Generated output
└── README.md            # Project documentation

🌐 Example Output

newsletter.html will contain:

    Top 3 TechCrunch articles

    Summaries with friendly tone

    "Subscribe for More" button

# 🧩 Customization

    Change RSS Feed:
    Edit this line in main.py:

rss_items = fetch_rss("https://techcrunch.com/feed/")

to any RSS URL.

Adjust Tone or Length:
Update the subscribers dictionary:

    subscribers = [
        {
            "email": "you@example.com",
            "preferences": ["AI"],
            "tone": "friendly",
            "length": "short"
        }
    ]

    Add Web Scraping:
    Use the scrape_website() function as needed.

# 💡 Future Improvements

    Relevance scoring with embeddings (LangChain + OpenAI)

    Translation support

    Multi-format export (PDF, text)

    Analytics and A/B testing

# 📄 License

Everything About AI License. Feel free to use and adapt.
# ✉️ Contact

For questions or contributions, open an issue or pull request me.
