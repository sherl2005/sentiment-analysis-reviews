from scraping.amazon_scraper import get_amazon_reviews, save_reviews_to_csv
from src.preprocessing import preprocess_reviews

if __name__ == "__main__":
    asin = "B07DJHV6VZ"
    reviews = get_amazon_reviews(asin, pages=3)
    save_reviews_to_csv(reviews, "data/raw/amazon_reviews.csv")
    preprocess_reviews("data/raw/amazon_reviews.csv", "data/processed/amazon_reviews_cleaned.csv")