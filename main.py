import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

nltk.download('punkt')
nltk.download('stopwords')

# Use Indonesian stopword file
stop_words = set(stopwords.words('indonesian'))

# Define stemming function with Sastrawi
stemmer = StemmerFactory().create_stemmer()

# Preprocessing functions
def preprocess_text(text):
    # Tokenization and stemming
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens if token.isalpha()]

    # Remove stopwords and non-alphabetic tokens
    preprocessed_tokens = [token.lower() for token in stemmed_tokens if token.lower() not in stop_words]

    # Join tokens back into a single string
    preprocessed_text = ' '.join(preprocessed_tokens)

    return preprocessed_text

# Load data from CSV file
csv_file = 'quran.csv'
excel_file = 'quran.xlsx'
translation_column = 'translation'  # The column to analyze
verse_key_column = 'verse_key'

# Create FastAPI instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quran Search API!"}

@app.get("/search")
def search_documents(query: str, total: int = 5):
    # Preprocess query
    preprocessed_query = preprocess_text(query)

    # Load data from CSV file
    data_frame = pd.read_csv(csv_file)

    # Load data from Excel file
    original_data_frame = pd.read_excel(excel_file, sheet_name='Sheet1')

    # Fill NaN values with empty string in translation_column
    data_frame[translation_column] = data_frame[translation_column].fillna('')

    # Extract text data from the specified column
    documents = data_frame[translation_column].tolist()
    original_documents = original_data_frame[translation_column].tolist()
    verse_keys = data_frame[verse_key_column].tolist()

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    # Fit the vectorizer on the documents
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Preprocess query and transform it using the vectorizer
    query_vector = vectorizer.transform([preprocess_text(query)])

    # Calculating Cosine Similarity
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)

    # Ranking and Retrieval
    similarities = cosine_similarities[0]
    top_indices = similarities.argsort()[::-1][:total]
    results = []

    for idx in top_indices:
        if idx < len(original_documents):
            doc = original_documents[idx]
            verse_key = verse_keys[idx]
            score = similarities[idx]
            result = {
                "verse_key": verse_key,
                "document": doc,
                "similarity_score": score
            }
            results.append(result)

    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=25117)
