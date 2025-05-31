class Movies:
    def __init__(self):
        self.movies = []
    
    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'

comedy = Comedy()
comedy_film = comedy.add_movie('Большой куш')
print(comedy_film)

drama = Drama()
drama_film = drama.add_movie('Оружейный барон')
print(drama_film)