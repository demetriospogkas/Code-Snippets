### Locate bad UTF-8 encoding
### Kudos: 
>>> file = {file_dir}
UnicodeDecodeError: 'utf-8' codec can't decode byte {byte} in position {position}: invalid continuation byte

>>> with open(file, 'r') as inputFile:
>>>    data = inputFile.read()

>>> from pprint import pprint
>>> f = open(file, 'rb')
>>> f.seek({position})
>>> pprint(f.read(500))
