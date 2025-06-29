# main.py

import feedparser
import requests
from bs4 import BeautifulSoup
from jinja2 import Template

# Fetch RSS Feed
def fetch_rss(feed_url, limit=5):
    feed = feedparser.parse(feed_url)
    entries = feed.entries[:limit]
    return [{"title": e.title, "link": e.link, "summary": e.summary} for e in entries]

# Web Scraping (optional example)
def scrape_website(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    paragraphs = [p.text.strip() for p in soup.find_all('p')]
    return " ".join(paragraphs[:3])

# Tone Adjustment
def adjust_tone(text, tone):
    if tone == "friendly":
        return "Hey there! " + text
    elif tone == "formal":
        return "Greetings. " + text
    else:
        return text

# Length Trimming
def trim_length(text, length):
    if length == "short":
        return text[:200] + "..."
    return text

# Simple inline HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; }
    .section { margin-bottom: 20px; }
    .cta { background: #007BFF; color: white; padding: 10px; display: inline-block; text-decoration: none; }
  </style>
</head>
<body>
  <h1>{{ title }}</h1>
  {% for section in sections %}
  <div class="section">
    <h2>{{ section.title }}</h2>
    <p>{{ section.summary }}</p>
    <a href="{{ section.link }}">Read more</a>
  </div>
  {% endfor %}
  <a class="cta" href="{{ cta_link }}">{{ cta_text }}</a>
</body>
</html>
"""

def main():
    # Example subscriber preferences
    subscribers = [
        {
            "email": "alice@example.com",
            "preferences": ["AI", "Blockchain"],
            "tone": "friendly",
            "length": "short"
        }
    ]
    subscriber = subscribers[0]

    # Fetch RSS feed
    rss_items = fetch_rss("https://techcrunch.com/feed/")

    # Use the fetched items directly
    ranked = rss_items

    # Prepare sections
    sections = []
    for item in ranked[:3]:
        summary = adjust_tone(
            trim_length(item["summary"], subscriber["length"]),
            subscriber["tone"]
        )
        sections.append({
            "title": item["title"],
            "summary": summary,
            "link": item["link"]
        })

    # Render newsletter
    template = Template(html_template)
    html = template.render(
        title="Your Weekly Digest",
        sections=sections,
        cta_text="Subscribe for More",
        cta_link="https://yournewsletter.com/subscribe"
    )

    # Save newsletter
    with open("newsletter.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ Newsletter generated successfully! Check 'newsletter.html'.")

if __name__ == "__main__":
    main()
