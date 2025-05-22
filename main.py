import sys
import os
import pandas as pd
from data_loader import generate_sample_reviews
from src.preprocessing import preprocess_reviews
from src.labeling import label_cleaned_reviews
from src.modeling import train_models

def main():
    raw_path = "data/raw/amazon_reviews.csv"
    cleaned_path = "data/processed/amazon_reviews_cleaned.csv"
    labeled_path = "data/processed/labeled_reviews.csv"
    
    # Step 1: Generate synthetic reviews for testing
    reviews = generate_sample_reviews()
    
    # Step 2: Ensure the raw reviews are saved
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    if not os.path.exists(raw_path):
        pd.DataFrame({"review": reviews}).to_csv(raw_path, index=False)
    print(f"✅ Raw reviews available at {raw_path}")
    
    # Step 3: Preprocess reviews
    preprocess_reviews(raw_path, cleaned_path)
    
    # Step 4: Label reviews
    label_cleaned_reviews(cleaned_path, labeled_path)
    
    # Step 5: Train models
    if os.path.exists(labeled_path) and pd.read_csv(labeled_path).shape[0] > 0:
        train_models(labeled_path)
    else:
        print(f"⚠️ No labeled data in {labeled_path}. Skipping training.")

if __name__ == "__main__":
    main()
