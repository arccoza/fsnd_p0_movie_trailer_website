import pystache
import models


with open('./movies.html.mustache', 'r') as fin:
  with open('./movies.html', 'w') as fout:
    fout.write(pystache.render(fin.read(), {'movies': models.movies}))
