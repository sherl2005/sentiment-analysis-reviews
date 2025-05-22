import pandas as pd

def heuristic_label(text):
    positive_words = ["good", "great", "excellent", "love", "amazing", "nice", "perfect", "happy", "awesome"]
    negative_words = ["bad", "poor", "terrible", "hate", "worst", "broken", "disappointed", "slow", "return"]

    text = text.lower()
    pos_count = sum(word in text for word in positive_words)
    neg_count = sum(word in text for word in negative_words)

    if pos_count > neg_count:
        return 1  # Positive
    elif neg_count > pos_count:
        return 0  # Negative
    else:
        return -1  # Neutral or ambiguous

def label_cleaned_reviews(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Apply heuristic labeling
    df["label"] = df["cleaned_review"].apply(heuristic_label)

    # Drop ambiguous/neutral rows
    df = df[df["label"] != -1]

    df.to_csv(output_csv, index=False)
    print(f"Labeled reviews saved to {output_csv} with {len(df)} rows.")

if __name__ == "__main__":
    input_file = "data/processed/amazon_reviews_cleaned.csv"
    output_file = "data/processed/labeled_reviews.csv"
    label_cleaned_reviews(input_file, output_file)
