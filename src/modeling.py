import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import sys


def train_models(labeled_csv):
    df = pd.read_csv(labeled_csv)

    if df.empty:
        print(f"No labeled data in {labeled_csv}. Skipping training.")
        return

    X = df["cleaned_review"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Naïve Bayes
    nb = MultinomialNB()
    nb.fit(X_train_tfidf, y_train)
    y_pred_nb = nb.predict(X_test_tfidf)
    print("=== Naïve Bayes ===")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_nb):.4f}")
    print(classification_report(y_test, y_pred_nb))

    # Logistic Regression
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train_tfidf, y_train)
    y_pred_lr = lr.predict(X_test_tfidf)
    print("=== Logistic Regression ===")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_lr):.4f}")
    print(classification_report(y_test, y_pred_lr))


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/processed/labeled_reviews.csv"
    train_models(path)