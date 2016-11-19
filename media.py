import tmdbsimple as tmdb
from tmdbsimple import Search, Movies
from pprint import pprint
from requests import HTTPError


class Movie(dict):
  def __init__(self, **kwargs):
    # Ensure keys and values are unicode.
    kwargs = {unicode(k): unicode(v) for k, v in kwargs.iteritems()}
    super(Movie, self).__init__(**kwargs)

    self._posters_url = 'https://image.tmdb.org/t/p/w640'
    self._videos_url = 'https://www.youtube.com/watch?v='

    for k, v in self.iteritems():
      if k == 'title':
        return
    raise MovieInitError('You must at least provide a title.')

  def lookup(self):
    try:
      res = search.movie(query=self['title'])
      res = Movies(res['results'][0]['id']).info(append_to_response='videos')
    except (IndexError, HTTPError):
      raise MovieSearchError(
        'Could not retrieve info on movie: "' + self['title'] + '"')

    res.update(self)
    self.update(res)

    self[u'poster_url'] = self.get('poster_url') or self._posters_url + self['poster_path']
    if 'trailer_url' not in self:
      for v in self['videos']['results']:
        if(v['site'] == u'YouTube' and v['type'] == u'Trailer'):
          self[u'trailer_url'] = self._videos_url + v[u'key']
          break


class MovieInitError(Exception):
  def __init__(self, message, errors=None):
    super(MovieInitError, self).__init__(message)
    self.errors = errors


class MovieSearchError(Exception):
  def __init__(self, message, errors=None):
    super(MovieSearchError, self).__init__(message)
    self.errors = errors


tmdb.API_KEY = '2874d8e2341ae3de760cc2119047fbb0'
search = Search()
# Movie.fetch_details('The Fifth Element')
# m = Movie(title='The Fifth Element')
# m = Movie([('title', 'The Fifth Element')])
# m.lookup()
# pprint(m)
