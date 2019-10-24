# DAVIDRVU - 2019

# FROM PANDAS DATAFRAME TO HTML

import io
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(
    randn(5, 4),
    index = 'A B C D E'.split(),
    columns = 'W X Y Z'.split()
)

str_io = io.StringIO()

df.to_html(buf=str_io, classes='table table-striped')

html_str = str_io.getvalue()

print(html_str)
