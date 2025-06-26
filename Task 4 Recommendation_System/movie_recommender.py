import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
movies = pd.DataFrame({
    "title": [
        "The Matrix", "John Wick", "Toy Story", "Finding Nemo",
        "Inception", "The Godfather", "Avengers: Endgame",
        "Interstellar", "Shrek", "The Dark Knight"
    ],
    "genre": [
        "Action Sci-Fi", "Action Thriller", "Animation Comedy",
        "Animation Adventure", "Action Sci-Fi", "Crime Drama",
        "Action Sci-Fi Superhero", "Sci-Fi Drama", "Animation Comedy",
        "Action Crime Thriller"
    ]
})

# TF-IDF vectorization on genres
vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])
similarity = cosine_similarity(genre_matrix)

# Recommendation function
def recommend(movie_title, movies, similarity_matrix, top_n=3):
    movie_title = movie_title.strip().lower()
    movies["title_lower"] = movies["title"].str.strip().str.lower()
    
    if movie_title not in movies["title_lower"].values:
        print(f"\nSorry, the movie '{movie_title}' was not found in our dataset.")
        print("Available movies:")
        for title in movies["title"]:
            print(" -", title)
        return None

    idx = movies[movies["title_lower"] == movie_title].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_movies = [movies.iloc[i[0]]["title"] for i in sim_scores[1:top_n + 1]]

    return top_movies

# User input and results
user_input = input("Enter a movie title: ").strip()

if not user_input:
    print("No input provided. Please try again.")
else:
    recommendations = recommend(user_input, movies, similarity)

    if recommendations:
        print(f"\nBecause you watched '{user_input}', you might also like:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    else:
        print("\nNo recommendations found. Try another movie from the list.")

# Safe exit for both interactive and non-interactive environments
try:
    input("\nPress Enter to exit...")
except EOFError:
    pass
