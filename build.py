'''
Refs:
  http://stackoverflow.com/questions/12517451/python-automatically-creating-directories-with-file-output
'''
import pystache
import models
import os
import errno


# with open('./src/movies.html', 'r') as fin:
#   with open('./movies.html', 'w') as fout:
#     fout.write(pystache.render(fin.read(), {'movies': models.movies}))

src = os.path.abspath('./src')
dest = os.path.abspath('./pub')

# print('bob'.split('bo'))

for root, dirs, files in os.walk(src):
  for f in files:
    with open(f, 'r') as fin:
      tail = root.split(src)[1]
      final_dest = os.path.abspath(dest + tail)

      try:
        os.makedirs(final_dest)
      except OSError as ex:
        if ex.errno != errno.EEXIST:
            raise

      final_dest += '/' + f
      print(final_dest)
      with open(final_dest, 'w') as fout:
        fout.write(pystache.render(fin.read(), {'movies': models.movies}))
