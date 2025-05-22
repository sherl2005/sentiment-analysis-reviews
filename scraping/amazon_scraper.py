import requests
from bs4 import BeautifulSoup
import time
import random
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

def get_amazon_reviews(asin, pages=1):
    all_reviews = []
    for page in range(1, pages + 1):
        url = f"https://www.amazon.in/product-reviews/{asin}/?pageNumber={page}"
        print(f"Scraping {url}")
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        reviews = soup.find_all("span", {"data-hook": "review-body"})

        for r in reviews:
            text = r.get_text(strip=True)
            all_reviews.append(text)

        time.sleep(random.uniform(1, 3))

    return all_reviews

def save_reviews_to_csv(reviews, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["review"])
        for review in reviews:
            writer.writerow([review])

if __name__ == "__main__":
    asin = "B07DJHV6VZ"  # Example: Echo Dot
    reviews = get_amazon_reviews(asin, pages=5)
    save_reviews_to_csv(reviews, "data/raw/amazon_reviews.csv")
