from scraping.amazon_scraper import get_amazon_reviews, save_reviews_to_csv

if __name__ == "__main__":
    asin = "B07DJHV6VZ"
    reviews = get_amazon_reviews(asin, pages=3)
    save_reviews_to_csv(reviews, "data/raw/amazon_reviews.csv")
