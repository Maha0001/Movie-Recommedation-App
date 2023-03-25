# 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

import openai
import streamlit as st

openai.api_key = "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"

def generate_recommendations(genre, year, limit):
    prompt = f"Generate a list of {limit} Hollywood movies and TV-Series in the {genre} genre released between {year} and 2022."
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=3000,
        n=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    choices = completions.choices[0].text.strip().split("\n")
    movies = [choice.strip() for choice in choices if choice.strip()]
    return movies[:limit]

st.title("Movie Recommendation App")

genre = st.selectbox("Select a genre", ["Programming","Articial Intelligence", "Action", "War", "Money", "Adult", "TV-Series", "Comedy", "Drama", "Horror", "Romance", "Science Fiction", "Thriller"])
year = st.slider("Select a release year", 1910, 2023, (1910, 2023))
limit = st.slider("Select the number of recommendations to generate", 10, 500, 50)

if st.button("Generate Recommendations"):
    movies = generate_recommendations(genre, year[0], limit)
    st.write(f"Here are your {len(movies)} recommendations:")
    for i, movie in enumerate(movies):
        st.write(f"{i+1}. {movie.split('.')[1].strip()}")
