from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import random

def get_flipkart_reviews(product_url, pages=3):
    driver = webdriver.Chrome()
    driver.get(product_url)
    all_reviews = []

    for _ in range(pages):
        time.sleep(random.uniform(2, 4))
        reviews = driver.find_elements(By.CLASS_NAME, "_6K-7Co")
        all_reviews += [r.text for r in reviews if r.text.strip()]

        try:
            next_button = driver.find_element(By.CLASS_NAME, "_1LKTO3").find_elements(By.TAG_NAME, "a")[-1]
            next_button.click()
        except:
            print("No more pages.")
            break

    driver.quit()
    return all_reviews

def save_reviews_to_csv(reviews, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["review"])
        for review in reviews:
            writer.writerow([review])

if __name__ == "__main__":
    url = "https://www.flipkart.com/product-reviews/ITEM_ID_HERE"  # replace with actual product review page
    reviews = get_flipkart_reviews(url, pages=5)
    save_reviews_to_csv(reviews, "data/raw/flipkart_reviews.csv")
