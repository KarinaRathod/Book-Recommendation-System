
# 📚 AI Book Recommendation System

A machine learning-powered web application built with Streamlit that recommends books based on user preferences. By selecting a book you have enjoyed, the system uses collaborative filtering (or content-based filtering) to suggest similar titles.

## ✨ Features
* **Top Charts:** View the current top 10 most popular books.
* **Smart Recommendations:** Select a book from the dropdown to instantly get personalized suggestions.
* **Interactive UI:** Clean, responsive design built specifically for book lovers.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Cosine Similarity)
* **Language:** Python 3.x

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/book-recommendation-system.git](https://github.com/yourusername/book-recommendation-system.git)
   cd book-recommendation-system

```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install the required dependencies:**
```bash
pip install -r requirements.txt

```


4. **Ensure your model files are present:**
Make sure your trained data files (e.g., `model.pkl`, `pt.pkl`, etc.) and datasets are placed in the correct directory as expected by `model.py`.
5. **Run the Streamlit app:**
```bash
streamlit run app.py

```



