import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_amazon_reviews(asin, max_pages=3):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/113.0.0.0 Safari/537.36"
        )
    }

    all_reviews = []

    for page in range(1, max_pages + 1):
        url = f"https://www.amazon.in/product-reviews/{asin}/?pageNumber={page}"
        print(f"Scraping {url}")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")

            # Save HTML for debugging
            os.makedirs("debug", exist_ok=True)
            with open(f"debug/debug_page_{page}.html", "w", encoding="utf-8") as f:
                f.write(soup.prettify())
            print(f"[Debug] Saved HTML snapshot to debug/debug_page_{page}.html")

            # Try multiple selectors
            reviews = soup.select("span[data-hook='review-body'] span")
            if not reviews:
                reviews = soup.select("div.review-data")
            if not reviews:
                reviews = soup.select(".review-text-content span")
                
            if not reviews:
                print(f"Warning: No reviews found on page {page}")
                continue

            for r in reviews:
                review_text = r.get_text(strip=True)
                if review_text:
                    all_reviews.append(review_text)

        except Exception as e:
            print(f"Error scraping page {page}: {e}")

    print(f"Total reviews scraped: {len(all_reviews)}")
    return all_reviews
