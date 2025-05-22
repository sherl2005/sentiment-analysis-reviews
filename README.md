# Sentiment Analysis on Product Reviews

## Description
This project performs sentiment analysis on product reviews scraped from Amazon and Flipkart. It includes traditional machine learning models (Naïve Bayes, Logistic Regression) and a fine-tuned DistilBERT for comparison.

## Structure

```
sentiment-analysis-reviews/
├── scraping/        # Scrapers for Amazon and Flipkart
├── data/            # Raw and processed data
├── src/             # Preprocessing, training, evaluation
├── notebooks/       # Jupyter notebooks for EDA and prototyping
├── main.py          # Entry point for preprocessing, training, prediction
```

## Setup

```bash
pip install -r requirements.txt
```

### Run the Amazon Scraper

```bash
python scraping/amazon_scraper.py
```

## ✅ `requirements.txt`

```
requests
beautifulsoup4
selenium
pandas
scikit-learn
nltk
spacy
transformers
datasets
streamlit
```