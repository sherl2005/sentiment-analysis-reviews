from scraping.amazon_scraper import get_amazon_reviews, save_reviews_to_csv
from src.preprocessing import preprocess_reviews
from src.labeling import label_cleaned_reviews
from src.modeling import train_models

if __name__ == "__main__":
    asin = "B07DJHV6VZ"
    reviews = get_amazon_reviews(asin, pages=3)
    save_reviews_to_csv(reviews, "data/raw/amazon_reviews.csv")
    preprocess_reviews("data/raw/amazon_reviews.csv", "data/processed/amazon_reviews_cleaned.csv")
    label_cleaned_reviews("data/processed/amazon_reviews_cleaned.csv", "data/processed/labeled_reviews.csv")
    train_models("data/processed/labeled_reviews.csv")