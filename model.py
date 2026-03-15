import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def prepare_model():

    # Load datasets
    books = pd.read_csv("Books.csv", low_memory=False)
    ratings = pd.read_csv("Ratings.csv")

    books = books[['ISBN', 'Book-Title', 'Book-Author', 'Image-URL-M']]

    # Merge books and ratings
    data = ratings.merge(books, on='ISBN')

    # -----------------------------
    # Filter active users
    # -----------------------------
    users = data.groupby('User-ID').count()['Book-Rating'] > 200
    active_users = users[users].index

    filtered = data[data['User-ID'].isin(active_users)]

    # -----------------------------
    # Filter popular books
    # -----------------------------
    books = filtered.groupby('Book-Title').count()['Book-Rating'] > 50
    popular_books = books[books].index

    final = filtered[filtered['Book-Title'].isin(popular_books)]

    # -----------------------------
    # Pivot Table
    # -----------------------------
    pt = final.pivot_table(
        index='Book-Title',
        columns='User-ID',
        values='Book-Rating'
    )

    pt.fillna(0, inplace=True)

    # Cosine similarity
    similarity = cosine_similarity(pt)

    # -----------------------------
    # Popular books list
    # -----------------------------
    popular = data.groupby('Book-Title').agg({
        'Book-Rating': 'count'
    }).reset_index()

    popular = popular.rename(columns={'Book-Rating': 'num_ratings'})
    popular = popular.sort_values('num_ratings', ascending=False)

    return pt, similarity, popular


def recommend(book_name, pt, similarity):

    index = pt.index.get_loc(book_name)

    distances = similarity[index]

    books = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended = []

    for i in books:
        recommended.append(pt.index[i[0]])

    return recommended