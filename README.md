## Live Demo
link->https://movies-recommendation-system-axdg.onrender.com
# 🎬 Movie Recommendation System

> A Machine Learning-based Movie Recommendation System built with Python and Streamlit that recommends similar movies using Content-Based Filtering.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?logo=pandas)

---

## 📌 Overview

The Movie Recommendation System is a Machine Learning project that recommends movies similar to a movie selected by the user.

The recommendation engine is built using **Content-Based Filtering**, where movies are compared based on their metadata such as genres, keywords, cast, crew, and overview. After selecting a movie from the dropdown menu in the Streamlit application, the system recommends the **Top 5 most similar movies**.

The complete data preprocessing, feature engineering, and model building were performed in **Jupyter Notebook**, while the interactive user interface was developed using **Streamlit**.

---

## ✨ Features

- 🎥 Select a movie from a dropdown menu
- 🤖 Recommend Top 5 similar movies
- ⚡ Fast recommendations using precomputed similarity matrix
- 💻 Interactive Streamlit web interface
- 📊 Content-Based Recommendation System
- 📁 Machine Learning model saved using Pickle

### 🚀 Planned Features

- 🖼 Display movie posters with recommendations
- ⭐ Movie ratings
- 📅 Release year
- 🎭 Genre information
- ❤️ Favorite movies
- 🌙 Dark mo

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| IDE | Jupyter Notebook, VS Code |
| Frontend | Streamlit |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| NLP | CountVectorizer |
| Similarity Metric | Cosine Similarity |
| Model Storage | Pickle (.pkl) |
| Dataset | Kaggle TMDB Movie Dataset |

---

## 📂 Project Workflow

```text
Kaggle Dataset
      │
      ▼
Data Cleaning
(Jupyter Notebook)
      │
      ▼
Feature Engineering
      │
      ▼
Create Tags
      │
      ▼
CountVectorizer
      │
      ▼
Cosine Similarity
      │
      ▼
Save Model (.pkl)
      │
      ▼
Streamlit Web Application
      │
      ▼
Top 5 Movie Recommendations
```

---

## 📁 Project Structure

```
Movie-Recommendation-System/
│
├── app.py                      # Streamlit application
├── Untiled.ipynb               # (movie recommendation notebook) Data preprocessing & model building
├── movies.csv                  # Processed movie dataset
├── similarity.pkl              # Similarity matrix
├── requirements.txt
├── README.md
├── .gitignore
└── images/                     # it contain live screenshots of my project
```

---

## ⚙️ How It Works

### Step 1 — Dataset

The project uses the **TMDB Movie Metadata Dataset** downloaded from Kaggle.

### Step 2 — Data Preprocessing

The dataset is cleaned by:

- Removing missing values
- Merging movie and credits datasets
- Extracting useful information

### Step 3 — Feature Engineering

Important movie features are combined into a single text column:

- Genres
- Keywords
- Cast
- Director
- Overview
- etc

### Step 4 — Text Vectorization

The combined text is converted into numerical vectors using **CountVectorizer**.

### Step 5 — Similarity Calculation

Cosine Similarity is calculated between all movies to determine how similar they are.

### Step 6 — Recommendation

When a user selects a movie from the Streamlit interface, the application:

- Finds the selected movie
- Computes similarity scores
- Returns the Top 5 most similar movies

---


## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/diwakar221718/Movies-Recommendation-system
```

Move into the project directory

```bash
cd movie-recommendation-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```
---

## 📊 Dataset

Source:

- TMDB Movie Metadata Dataset (Kaggle)

Dataset includes:

- Movie Titles
- Genres
- Cast
- Crew
- Keywords
- Overview
- Ratings
- Release Date

---

## 🎯 Skills Demonstrated

- Data Cleaning
- Feature Engineering
- Machine Learning
- Recommendation Systems
- Streamlit Development
- Model Serialization
- Git & GitHub
- Python Programming

---

## 💡 Challenges Faced

- Handling missing values
- Combining multiple datasets
- Building an efficient recommendation engine
- Integrating ML model with Streamlit

---

## 🔮 Future Improvements

- Display movie posters
- Integrate TMDB API
- Show IMDb ratings
- Movie trailers
- Hybrid Recommendation System
- Collaborative Filtering
- User Authentication
- Personalized recommendations
- Responsive UI
- Cloud deployment

---

## 👨‍💻 Author


📧 Email: dyadav221718@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/diwakar-yadav-58aba7284/

💻 GitHub: https://github.com/diwakar221718

---

## ⭐ Show Your Support

If you found this project useful, please consider giving it a ⭐ on GitHub!
