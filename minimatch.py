'''A minimatch.js like globbing module.'''
import re
import fnmatch
import os


def _rng_repl(match):
  m = match.groupdict()
  return '[' + ('^' if m['neg'] else '') + m['rng'] + ']'

_os_is_win = True if os.name == 'nt' else False
_sep = '{sep}'
_real_sep = r'\\' if _os_is_win else '/'
_any = '[^' + _sep + ']'
_evr = '[^' + _sep + ']*?'
_dbl = '**'
_dbl_repl = '.*?'
_oth = [
  ('_qum', '\?', _any),
  ('_str', '\*', _evr),
  ('_rng', '\[(?P<neg>[\^!])?(?P<rng>[\d\w-]*?)\]', _rng_repl)
]


def _convert(pats):
  '''Takes parts of a glob pattern and converts it to a regex.'''
  for pat in pats:
    if pat == '':
      continue
    elif pat == _dbl:
      yield _dbl_repl
      continue
    for k, v, repl in _oth:
      res = re.sub(v, repl, pat)
      # print(k)
      # if res is not pat:
      #   print('--' + k)
      pat = res
    yield pat


def _compile(glob):
  '''
  Takes a glob pattern and compiles it into a regex string,
  returns the regex string.
  '''
  regex = []
  parts = re.split('/*', glob)
  # print(parts)

  if _os_is_win and parts[0] == '':
    regex.append('.:')

  for i, part in enumerate(_convert(parts)):
    if i > 0 or parts[0] == '':
      regex.append(_sep)
    regex.append(part)

  if parts[-1] == '':
    regex.append(_sep)
  # print(regex)
  return ''.join(regex).format(**{_sep[1:-1]: _real_sep})


def minimatch(path, pat):
  '''
  Takes a file path and compares it to a glob pattern,
  if there is a match it returns the match obj otherwise None.

  Args:
    path (str): The path to check against pat.
    pat (str): The pat to test path with.

  Returns:
    A match object if successful, None otherwise.
  '''
  pat = _compile(pat)
  # print(pat)
  return re.match(pat, path)


# print(minimatch('/bob/sam/foo.txt', '/**/foo.t?t'))
# print(minimatch('c:\\bob\\sam\\foo.txt', '/**/foo.t?t'))
