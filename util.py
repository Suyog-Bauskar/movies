import pandas as pd
from tabulate import tabulate


def init():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)


def display_all_movies():
    df = pd.read_csv("movies.csv", index_col=False, header=0)
    print(tabulate(df, showindex=False, headers=df.columns))


def display_menu():
    print()
    print("-------------------------------------------------------------------")
    print("1. Display All Movies")
    print("2. Display Top 10 Rows of The Dataset")
    print("3. Display Last 10 Rows of The Dataset")
    print("4. Find Shape of Our Dataset (Number of Rows And Number of Columns)")
    print("5. Display Top 10 Highest Rated Movies")
    print("6. Exit")
    print("-------------------------------------------------------------------")


def display_top_10_rows():
    pass


def display_last_10_rows():
    pass


def find_shape_of_dataset():
    pass


def display_top_10_highest_rated_movies():
    pass
