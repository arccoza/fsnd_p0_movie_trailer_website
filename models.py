from media import Movie


movies = [
  Movie(title='The Fifth Element'),
  Movie(title='The Dirty Dozen'),
  Movie(title='Escape from New York')
]

for m in movies:
  m.lookup()
