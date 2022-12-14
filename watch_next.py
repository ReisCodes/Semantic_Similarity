import spacy  # Import SpaCy module

nlp = spacy.load('en_core_web_md')  # Import English model


# This Function takes the description of a movie as a parameter and returns a suggestion for what movie to watch next
def movie_suggestion(user_movie_description):
    # Open the txt file containing movie suggestions and save the descriptions to a list
    file = open("movies.txt", "r", encoding="utf-8")
    list_of_movies = []
    for movie in file:
        movie_description = movie.strip()
        list_of_movies.append(movie_description[9:])
    file.close()

    model_description = nlp(user_movie_description)  # Pass the description through the language model

    # Compare similarity of old movie to descriptions of new movies
    list_of_similarity_scores = []  # Store the similarity scores in an empty list
    for movie in list_of_movies:
        similarity = nlp(movie).similarity(model_description)
        list_of_similarity_scores.append(similarity)

    # Locate the movie with the highest similarity score and display this suggestion to the user
    highest_movie_index = list_of_similarity_scores.index(max(list_of_similarity_scores))
    with open("movies.txt", "r", encoding="utf-8") as file:
        movie_to_suggest_description = file.readlines()[highest_movie_index]
        movie_to_suggest = movie_to_suggest_description[:7]

    print(f"Given the description of the movie you just watched, we suggest you watch {movie_to_suggest} next!"
          f"\n\n{movie_to_suggest} description:"
          f"\n{movie_to_suggest_description[9:]}")


planet_hulk_description = """
    Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick
    the Hulk into a shuttle and launch him into space to a plant where the Hulk can live in peace. Unfortunately, Hulk 
    land on planet Sakaar where he is sold into slavery and trained as a gladiator.  
    """

# Run the function with the description above
movie_suggestion(planet_hulk_description)
