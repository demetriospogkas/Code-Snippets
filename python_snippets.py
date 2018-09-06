### Locate bad UTF-8 encoding
### Kudos: https://stackoverflow.com/questions/46180610/python-3-unicodedecodeerror-how-do-i-debug-unicodedecodeerror
>>> file = ${file_dir}
UnicodeDecodeError: 'utf-8' codec can't decode byte ${byte} in position ${position}: invalid continuation byte

>>> with open(file, 'r') as inputFile:
>>>    data = inputFile.read()

>>> from pprint import pprint
>>> f = open(file, 'rb')
>>> f.seek(${position})
>>> pprint(f.read(500))

### Regex groups substitution
import re
re.sub('(\d{2})/(\d{2})/(\d{4})', '\g<3>-\g<1>-\g<2>', ${a_date_string})

### Pandas groupby and value_counts with multiple columns
### Kudos: https://stackoverflow.com/questions/42998660/pandas-how-to-groupby-with-count-with-multiple-levels-on-rows
import pandas as pd
df = pd.DataFrame(...)
df.groupby([${col1}, ${col2}, ${col3}]).size().unstack().stack(dropna=True).reset_index(name="Count")

### Pandas sort by multiple columns with multiple different ascending values
### Kudos: https://stackoverflow.com/questions/17141558/how-to-sort-a-dataframe-in-python-pandas-by-two-or-more-columns
df.sort_values(by=[${col1}, ${col2}, ${col3}], ascending=[${True/False}, ${True/False}, ${True/False}], inplace=True)

### Increase Jupyter Notebook window size
### Kudos: https://stackoverflow.com/questions/21971449/how-do-i-increase-the-cell-width-of-the-jupyter-ipython-notebook-in-my-browser/34058270#34058270
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:70% !important; }</style>"))
