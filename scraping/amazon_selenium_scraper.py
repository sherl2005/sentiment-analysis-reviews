from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def scrape_amazon_reviews_selenium(asin, max_pages=3):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    
    driver = webdriver.Chrome(options=options)
    all_reviews = []
    
    try:
        for page in range(1, max_pages + 1):
            url = f"https://www.amazon.in/product-reviews/{asin}/?pageNumber={page}"
            print(f"Scraping {url} with Selenium")
            
            driver.get(url)
            time.sleep(5)  # Wait for page to load
            
            # Save screenshot for debugging
            os.makedirs("debug", exist_ok=True)
            driver.save_screenshot(f"debug/screenshot_page_{page}.png")
            
            # Save HTML for debugging
            with open(f"debug/selenium_page_{page}.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            
            try:
                # Wait for reviews to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-hook='review']"))
                )
                
                # Get all reviews
                review_elements = driver.find_elements(By.CSS_SELECTOR, "[data-hook='review-body']")
                
                if not review_elements:
                    print(f"Warning: No reviews found on page {page}")
                    continue
                    
                for element in review_elements:
                    review_text = element.text.strip()
                    if review_text:
                        all_reviews.append(review_text)
                        
            except Exception as e:
                print(f"Error processing page {page}: {e}")
                
            time.sleep(2)  # Be nice to the server
            
    finally:
        driver.quit()
        
    print(f"Total reviews scraped with Selenium: {len(all_reviews)}")
    return all_reviews