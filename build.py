'''
Refs:
  http://stackoverflow.com/questions/12517451/python-automatically-creating-directories-with-file-output
'''
import pystache
import models
import os
import shutil
import errno


src = os.path.abspath('./src')
dest = os.path.abspath('./pub')
data = {'movies': models.movies}

# Remove the previous build if it exists.
try:
  shutil.rmtree(dest)
except OSError as ex:
  if ex.errno != errno.ENOENT:
    raise

# Walk the src dir looking for html templates.
for root, dirs, files in os.walk(src):
  for f in files:
    with open(os.path.join(root, f), 'r') as fin:
      tail = root.split(src)[1]
      final_dest = os.path.abspath(dest + tail)

      # If the path doesn't exist create it.
      try:
        os.makedirs(final_dest)
      except OSError as ex:
        if ex.errno != errno.EEXIST:
            raise

      final_dest += '/' + f
      print(final_dest)
      with open(final_dest, 'w') as fout:
        fout.write(pystache.render(fin.read(), data))
