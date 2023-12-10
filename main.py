import pandas as pd
from tabulate import tabulate

df = pd.read_csv("movies.csv", index_col=False, header=0)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

print(tabulate(df, showindex=False, headers=df.columns))
