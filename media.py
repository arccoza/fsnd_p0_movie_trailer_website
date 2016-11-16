class Movie(object):
  def __init__(self, title, summary=None, poster_url=None, trailer_url=None):
    self.title = title
    self.summary = summary
    self.poster_url = poster_url
    self.trailer_url = trailer_url
