# Importing the class Movie from media file
from media import Movie

# Importing function open movies
import fresh_tomatoes as fm


# Making the instances of Movie
film1 = Movie("007 Sky Fall", "https://upload.wikimedia.org/wikipedia/pt/thumb/4/4a/Skyfall007.jpg/260px-Skyfall007.jpg",
              "https://youtu.be/6kw1UVovByw")
film2 = Movie("Titanic", "https://upload.wikimedia.org/wikipedia/pt/thumb/2/22/Titanic_poster.jpg/250px-Titanic_poster.jpg",
              "https://youtu.be/ZQ6klONCq4s")
film3 = Movie("Shrek", "https://upload.wikimedia.org/wikipedia/pt/thumb/e/e6/Shrek_Poster.jpg/200px-Shrek_Poster.jpg",
              "https://youtu.be/W37DlG1i61s")
film4 = Movie("Conde de monte cristo", "https://upload.wikimedia.org/wikipedia/pt/thumb/b/bb/The_Count_of_Monte_Cristo_film.jpg/250px-The_Count_of_Monte_Cristo_film.jpg", "https://youtu.be/X9F6Ssb7GHo")

# Inserting objects of Movie in a list
list = [film1, film2, film3, film4]


# Calling the function open_movies_page with the list parameter
fm.open_movies_page(list)
