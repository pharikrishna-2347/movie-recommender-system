# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Machine Learning, Natural Language Processing (NLP), and Streamlit.

The system recommends the top 5 most similar movies based on the movie selected by the user and also fetches their posters using the official TMDB API.

---

# 🚀 Live Demo

Deployed using Streamlit Community Cloud.
Try here now : - 
https://phk-movie-recommender-system-9xxye2tnmdv7kjc4b7y8sj.streamlit.app/


---

# 📌 Project Overview

This project was developed in two phases:

1. Data preprocessing and model creation using Jupyter Notebook
2. Web application development and deployment using Streamlit

The dataset used was the TMDB Movie Dataset from Kaggle containing information about 4800+ movies.

Initially, the dataset consisted of two separate CSV files with around 23 columns containing movie-related information such as:
- genres
- cast
- crew
- keywords
- overview
- movie id
- title
- and more

These datasets were cleaned, merged, and transformed into a simplified dataframe containing only:

- movie_id
- title
- tags

The `tags` column was created by combining useful textual information from multiple columns.

---

# 🧠 Machine Learning & NLP

The recommendation engine is based on Content-Based Filtering.

## Techniques Used

### 1. Text Vectorization

The tags column was vectorized using:

```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(
    max_features=5000,
    stop_words='english'
)
```

### 2. Stemming

Words were normalized using Porter Stemmer from NLTK.

```python
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
```

### 3. Cosine Similarity

Movie similarity was calculated using cosine similarity.

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)
```

When a user selects a movie, the system finds the 5 closest movies in the vector space based on cosine similarity.

---

# 🖼️ Movie Poster Fetching

Initially, the recommender system displayed only movie names.

To improve the user experience, movie posters were fetched dynamically using the official TMDB API.

The API returns the poster path for each movie using its movie ID.

```python
response = requests.get(url)
```

The top 5 recommended movies along with their posters are then displayed in the Streamlit web app.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- TMDB API
- Jupyter Notebook

---

# 📂 Project Structure

```bash
movie-recommender-system/
│
├── app.py
├── movies.pkl
├── movies_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── notebook.ipynb
```

---

# ⚡ Deployment

The application was deployed using:

- GitHub
- Streamlit Community Cloud

---

# 📊 Dataset

Dataset used:
TMDB 5000 Movie Dataset from Kaggle

Contains:
- 4800+ movies
- movie metadata
- cast and crew information

---

# 🎯 Features

✅ Content-Based Movie Recommendation  
✅ NLP-Based Similarity Matching  
✅ Cosine Similarity Recommendation Engine  
✅ Real-Time Poster Fetching using TMDB API  
✅ Interactive Streamlit UI  
✅ Cloud Deployment Support  

---

# 📸 Sample Workflow

1. User selects a movie
2. System converts movie tags into vectors
3. Cosine similarity scores are calculated
4. Top 5 similar movies are selected
5. Posters are fetched using TMDB API
6. Recommendations are displayed on the web app

---

# 🔮 Future Improvements

- Add collaborative filtering
- Improve recommendation accuracy
- Add movie trailers
- Add movie ratings and reviews
- Deploy using Docker and AWS
- Add search optimization

---

# 👨‍💻 Author

Hari Krishna
