import pandas as pd

# Expanded word lists + debug output

def heuristic_label(text):
    positive_words = [
        "good", "great", "excellent", "love", "amazing", "nice", "perfect",
        "happy", "awesome", "wonderful", "best", "satisfied", "recommend", "fast", "easy"
    ]
    negative_words = [
        "bad", "poor", "terrible", "hate", "worst", "broken", "disappointed",
        "slow", "return", "problem", "waste", "delay", "useless", "awful"
    ]

    text = str(text).lower()
    pos_count = sum(phrase in text for phrase in positive_words)
    neg_count = sum(phrase in text for phrase in negative_words)

    if pos_count > neg_count:
        return 1
    elif neg_count > pos_count:
        return 0
    else:
        return -1  # neutral or ambiguous


def label_cleaned_reviews(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Apply heuristic labeling
    df["label"] = df["cleaned_review"].apply(heuristic_label)

    # Debug prints
    print("Label counts before filtering (incl. neutral):")
    print(df["label"].value_counts(dropna=False))

    # Keep only positive/negative
    df = df[df["label"] != -1]

    print("Label counts after filtering neutral/ambiguous:")
    print(df["label"].value_counts())

    df.to_csv(output_csv, index=False)
    print(f"Labeled reviews saved to {output_csv} with {len(df)} rows.")


if __name__ == "__main__":
    import sys
    inp = sys.argv[1] if len(sys.argv) > 1 else "data/processed/amazon_reviews_cleaned.csv"
    out = sys.argv[2] if len(sys.argv) > 2 else "data/processed/labeled_reviews.csv"
    label_cleaned_reviews(inp, out)