import fresh_tomatoes as fm

class Movie():
    def __init__ (self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

film1 = Movie("007 Sky Fall", "https://upload.wikimedia.org/wikipedia/pt/thumb/4/4a/Skyfall007.jpg/260px-Skyfall007.jpg", "Link do trailer do filme")
film2 = Movie("Titanic", "https://upload.wikimedia.org/wikipedia/pt/thumb/2/22/Titanic_poster.jpg/250px-Titanic_poster.jpg", "Link do trailer do filme")
film3 = Movie("Shrek", "https://upload.wikimedia.org/wikipedia/pt/thumb/e/e6/Shrek_Poster.jpg/200px-Shrek_Poster.jpg", "Link do trailer do filme")
film4 = Movie("Conde de monte cristo", "https://upload.wikimedia.org/wikipedia/pt/thumb/b/bb/The_Count_of_Monte_Cristo_film.jpg/250px-The_Count_of_Monte_Cristo_film.jpg", "Link do trailer do filme")

lista = [film1,film2,film3,film4]

fm.open_movies_page(lista)
