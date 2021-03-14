import re

strr = 'an example word:cat!!'
pat = r'word:\w\w\w'

match = re.search(pat, strr)

if match:
    print('Found', match.group())
else:
    print('Did not find')
