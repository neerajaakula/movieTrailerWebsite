import media
import fresh_tomatoes

#Instances of favorite movies to be displayed on website
toyStory = media.Movie("Toy Story",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

bahubali2 = media.Movie("Bahubali 2",
                        "https://upload.wikimedia.org/wikipedia/en/8/8e/Baahubali_2_The_Conclusion.jpg",
                        "https://www.youtube.com/watch?v=qD-6d8Wo3do")

fateOfTheFurious = media.Movie("The Fate of the Furious",
                                  "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                                  "https://www.youtube.com/watch?v=qD-6d8Wo3do")


interstellar = media.Movie("Interstellar",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=0vxOhd4qlnA")

#list of all movie instances
movies = [toyStory, avatar, bahubali2, fateOfTheFurious, interstellar]

#calling the open_movies_page method of the fresh_tomatoes.py file to open HTML page with list of movies
fresh_tomatoes.open_movies_page(movies)

