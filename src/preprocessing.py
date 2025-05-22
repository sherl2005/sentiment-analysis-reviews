import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

nltk.download("punkt")
nltk.download("stopwords")

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]
    doc = nlp(" ".join(tokens))
    return " ".join([token.lemma_ for token in doc])

def preprocess_reviews(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df.dropna(inplace=True)
    df["cleaned_review"] = df["review"].apply(clean_text)
    df.to_csv(output_csv, index=False)
    print(f"Processed reviews saved to {output_csv}")
