Psuedocode programnya

```python
# import semua library yang dibutuhkan
import pandas, nltk, stop_words, word_tokenize, Sastrawi_StemmerFactory,sklearn, TfidfVectorizer, cosine_similarity

# Download package nltk
Download('punkt')
Download('stopwords')

# Set stopword bahasa indonesia
SET_STOPWORDS = 'indonesian'

# Set stemmer bahasa indonesia
SET_STEMMER = InitializeStemmer()

# Fungsi preprocessing data
FUNCTION preprocess_text(text)
    SET_TOKENS = Tokenizing(text)

    SET_TOKENS = [word.lower() for word in SET_TOKENS if word.isalpha() and word.lower() not in SET_STOPWORDS]

    SET_STEMMED = [SET_STEMMER.stem(word) for word in SET_TOKENS]

    preprocessed_text = ' '.join(SET_STEMMED)

    return preprocessed_text
END_FUNCTION

# Load dataset
SET_DATA = 'quran.xlsx' # format dataset adalah .xlsx atau excel
SET_DATA_COLUMN = 'translation' # nama kolom yang akan dijadikan data

# Konversi dataset ke dataframe
SET_DATAFRAME = Dataframe(SET_DATA)

# Ubah dataframe ke list
SET_DATAFRAME = SET_DATAFRAME[SET_DATA_COLUMN].tolist()

# Preprocessing Dokumen
SET_PREPROCESSED_DOCUMENT = [preprocess_text(document) for document in SET_DATAFRAME]

# Preprocessing Query atau pertanyaan dari user
SET_QUERY = Input('Iman dan takwa') # Contoh input dari user
PREPROCESSED_QUERY = preprocess_text(SET_QUERY)

# Inisialisasi TF-IDF Vectorizer
SET_TFIDF = TfidfVectorizer()

# Fit dan transform data
SET_TFIDF_MATRIX = SET_TFIDF.fit_transform(SET_PREPROCESSED_DOCUMENT)
SET_QUERY_TFIDF = SET_TFIDF.transform(PREPROCESSED_QUERY)

# Menghitung cosine similarity
SET_COSINE_SIMILARITY = cosine_similarity(SET_TFIDF, SET_TFIDF)

# Mengurutkan hasil cosine similarity
FOR i, query in enemurate(SET_QUERY):
  SET_SIMILARITY_SCORE = SET_COSINE_SIMILARITY[i]
  SORTED_SIMILARITY_SCORE = sorted(SET_SIMILARITY_SCORE, reverse=True)
  Output("Top 5 hasil pencarian untuk query " + query)

  IF SORTED_SIMILARITY_SCORE[0] == 0:
    Output("Tidak ada hasil pencarian")
  ELSE:
    FOR j, index in range(5):
      SET_DOCUMENT = SET_PREPROCESSED_DOCUMENT[index]
      SET_SCORE = SET_SIMILARITY_SCORE[index]
      Output("Dokumen ke-" + index + " dengan skor " + SET_SCORE + " adalah " + SET_DOCUMENT)
    END_FOR
  END_IF
END_FOR
```

## Penjelasan Library

- Pandas: Library untuk membaca dataset
- NLTK: Library untuk melakukan preprocessing data
- Sastrawi: Library untuk melakukan stemming
- TfidfVectorizer: Library untuk menghitung TF-IDF (Sklearn)
- Cosine Similarity: Library untuk menghitung cosine similarity (Sklearn)

## Tambahan

- Cari tahu apa itu supplementary material dan cara memasukannya ke dalam paper. Masukan link github ke supplementary material. Linknya `https://github.com/rayrama/sequran-ai`
