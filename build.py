'''
This is a simple build script that walks a source directory,
copying, and possibly manipulating, the files to a destination directory.
Refs:
  http://stackoverflow.com/questions/12517451/python-automatically-creating-directories-with-file-output
'''
import pystache
import models
import os
import shutil
import errno
from minimatch import minimatch


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
    in_path = os.path.join(root, f)
    with open(in_path, 'r') as fin:
      tail = root.split(src)[1]
      out_path = os.path.abspath(dest + tail)

      # If the path doesn't exist create it.
      try:
        os.makedirs(out_path)
      except OSError as ex:
        if ex.errno != errno.EEXIST:
            raise

      out_path += '/' + f
      print(out_path)
      with open(out_path, 'w') as fout:
        if minimatch(in_path, '/**/*.html'):
          fout.write(pystache.render(fin.read(), data))
        else:
          fout.write(fin.read())
