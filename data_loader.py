import pandas as pd
import os
import random

def generate_sample_reviews():
    """Generate a sample of synthetic Amazon reviews for testing"""
    print("Generating synthetic Amazon reviews dataset...")
    
    # Create directories if they don't exist
    os.makedirs("data/raw", exist_ok=True)
    
    # Sample positive reviews
    positive_reviews = [
        "This product exceeded my expectations. The quality is excellent and it works perfectly.",
        "I love this product! It's exactly what I needed and arrived quickly.",
        "Great value for money. Would definitely recommend to friends and family.",
        "Five stars! This is the best purchase I've made this year.",
        "The product is durable and well-designed. Very happy with my purchase.",
        "Works exactly as described. No issues whatsoever.",
        "Excellent customer service and a fantastic product.",
        "I've been using this for a month now and it still works like new.",
        "The setup was easy and the performance is outstanding.",
        "This product has made my life so much easier. Totally worth it!"
    ]
    
    # Sample negative reviews
    negative_reviews = [
        "Disappointed with the quality. It broke after just one week.",
        "Not worth the money. I regret this purchase.",
        "The product doesn't work as advertised. Would not recommend.",
        "Poor build quality and terrible customer service.",
        "Save your money and buy something else. This is junk.",
        "Arrived damaged and replacement process was a nightmare.",
        "The worst product I've ever bought. Complete waste of money.",
        "It stopped working after a few days. Very frustrating experience.",
        "The description is misleading. The actual product is much smaller.",
        "Overpriced and underperforming. Avoid this product."
    ]
    
    # Generate a dataset with 50 reviews (mix of positive and negative)
    all_reviews = []
    for _ in range(25):
        all_reviews.append(random.choice(positive_reviews))
    for _ in range(25):
        all_reviews.append(random.choice(negative_reviews))
    
    # Shuffle the reviews
    random.shuffle(all_reviews)
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame({"review": all_reviews})
    df.to_csv("data/raw/amazon_reviews.csv", index=False)
    print(f"✅ Generated {len(df)} sample reviews")
    return all_reviews