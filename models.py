from media import Movie


movies = [
  Movie(title='The Fifth Element'),
  Movie(title='The Dirty Dozen'),
  Movie(title='Escape from New York'),
  Movie(title='Serenity'),
  Movie(title='Kill Bill Vol. 1'),
  Movie(title='Kill Bill Vol. 2'),
  Movie(title='Cowboy Bebop'),
  Movie(title='Porco Rosso')
]

for m in movies:
  m.lookup()
