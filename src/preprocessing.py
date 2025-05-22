import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')  # Add this line to download the missing resource

try:
    nlp = spacy.load("en_core_web_sm")
except:
    import sys
    import subprocess
    print("Downloading spaCy model...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Use a simpler tokenization approach to avoid punkt_tab dependency
    tokens = text.split()
    tokens = [w for w in tokens if w not in stop_words]
    
    # Use spaCy for lemmatization
    doc = nlp(" ".join(tokens))
    return " ".join([token.lemma_ for token in doc])

def preprocess_reviews(input_csv, output_csv):
    print(f"Preprocessing reviews from {input_csv}...")
    df = pd.read_csv(input_csv)
    df.dropna(inplace=True)
    df["cleaned_review"] = df["review"].apply(clean_text)
    
    # Create directory if it doesn't exist
    import os
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    df.to_csv(output_csv, index=False)
    print(f"Processed reviews saved to {output_csv}")
