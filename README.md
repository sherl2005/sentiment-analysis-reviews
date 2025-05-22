# 🧠 Sentiment Analysis on E-Commerce Product Reviews

A modular, end-to-end sentiment analysis pipeline that classifies customer reviews as **positive** or **negative**. The project leverages publicly available Amazon datasets, web scraping, NLP preprocessing, and machine learning models to analyze real-world product feedback.

---

## 🚀 Project Highlights

### 🧩 Modular Architecture

The pipeline is organized into reusable modules:
- `scraping/`: Scripts to collect reviews from Amazon & Flipkart.
- `src/`: NLP preprocessing, labeling logic, and model training.
- `data_loader.py`: Handles data loading from JSON or CSV.
- `main.py`: Orchestrates the full pipeline.

### 🔍 Review Sources
- ✅ **Amazon Review Dataset (UCSD)**: Pre-labeled, large-scale product reviews.
- 🔧 Optional: Live web scraping from **Amazon** or **Flipkart** using `requests + BeautifulSoup` or `Selenium`.

---

## 🧪 Pipeline Overview

```plaintext
      ┌────────────┐
      │ Scraping   │ ◄───── Optional live scraping
      └────┬───────┘
           ▼
   ┌──────────────┐
   │ Data Loader  │ ◄───── From public JSON/CSV datasets
   └────┬─────────┘
        ▼
┌────────────────────┐
│ Preprocessing (NLP)│ ◄──── Text cleaning, lemmatization, stopword removal
└────┬───────────────┘
     ▼
┌────────────────────┐
│ Labeling (Heuristic)│ ◄──── Rule-based polarity scoring
└────┬────────────────┘
     ▼
┌────────────────────┐
│ Feature Extraction │ ◄──── TF-IDF (Word2Vec, BERT coming soon)
└────┬────────────────┘
     ▼
┌────────────────────┐
│ Model Training     │ ◄──── Naïve Bayes, Logistic Regression
└────────────────────┘
```

---

## 🛠️ How to Use

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sentiment-analysis-reviews.git
cd sentiment-analysis-reviews
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Load Amazon Dataset (Pre-scraped)

```python
from data_loader import load_real_amazon_reviews
df = load_real_amazon_reviews("data/raw/Video_Games.json")
```

Or use synthetic data:

```python
from data_loader import generate_sample_reviews
df = generate_sample_reviews()
```

### 4. Run the pipeline

```bash
python main.py
```

---

## 📦 Project Structure

```plaintext
sentiment-analysis-reviews/
├── data/
│   ├── raw/                 # Public Amazon datasets
│   └── processed/           # Cleaned and labeled reviews
├── scraping/
│   ├── amazon_scraper.py
│   ├── amazon_selenium_scraper.py
│   ├── flipkart_scraper.py
│   └── label_reviews.py
├── src/
│   ├── preprocessing.py     # Text normalization & tokenization
│   ├── labeling.py          # Heuristic-based sentiment labeling
│   ├── modeling.py          # ML models and evaluation
│   ├── embeddings.py        # (Coming soon: BERT, Word2Vec)
│   └── __init__.py
├── webapp/                  # (Coming soon: Streamlit/Flask app)
│   └── app.py
├── data_loader.py
├── main.py
└── README.md
```

---

## 🔮 Future Enhancements

* 🔁 **Embedding Support**: Word2Vec, BERT (via HuggingFace Transformers)
* 📈 **Experiment Tracking**: MLflow or Weights & Biases
* 💬 **Interactive App**: Streamlit/Flask app for live predictions
* 🧠 **Semi-Supervised Learning**: Improve labels using weak supervision
* 🗺️ **Visualizations**: Word clouds, attention maps, misclassified examples

---

## 📚 References

* [Amazon Review Dataset - Julian McAuley, UCSD](https://nijianmo.github.io/amazon/index.html)
* [NLTK](https://www.nltk.org/)
* [spaCy](https://spacy.io/)
* [scikit-learn](https://scikit-learn.org/)
* [HuggingFace Transformers](https://huggingface.co/transformers/)

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or improve.

---

## 📄 License

MIT License. See `LICENSE` for more details.

