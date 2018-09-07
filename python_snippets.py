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

### Hide axes in matplotlib plots
### Kudos: https://stackoverflow.com/questions/2176424/hiding-axis-text-in-matplotlib-plots
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

### Hide bounding box in matplotlib plots
### Kudos: https://stackoverflow.com/questions/14908576/how-to-remove-frame-from-matplotlib-pyplot-figure-vs-matplotlib-figure-frame/28720127#28720127
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

### Tight bounding box to plot in matplotlib
### Kudos: https://matplotlib.org/users/tight_layout_guide.html
plt.tight_layout(pad=0, w_pad=0, h_pad=0)

### Reading-Writing files:
with open(fname, 'r') as file:
    data = file.read()
    
with open(fname, 'w') as outfile:
    outfile.write(data)

### Drop rows based on conditions in pandas
### Kudos: https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression
df.drop(df[(df.score < 50) & (df.score > 20)].index, inplace=True)

### Delete a file if it exists
### Kudos: https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
try:
    os.remove(filename)
except OSError:
    # do something
