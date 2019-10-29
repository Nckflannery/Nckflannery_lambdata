'''
A collection of functions for DS8-Unit3-Sprint1
'''

import pandas as pd


def train_val_split(df, test_size=0.2):
    '''
    Returns two dataframes split by amount test_size
df = Pandas DataFrame to split
test_size = Size (number of rows) of returned 'test' DataFrame
after split (default = 0.2)
Example: train, test = train_val_split(df = pd.DataFrame, test_size = 0.3)
    '''
    size = round(test_size * len(df))
    test = df.sample(size)
    train = df.drop(test.index)
    return train, test


def is_null(df, sum=False):
    '''
    Checks and returns which items in a given dataframe are null
df = Pandas DataFrame
sum(bool) = Return the sum of nulls (True), or dataframe of nulls (False),
default=False
    '''
    nulls = (df != df)
    if sum is True:
        return nulls.sum()
    return nulls
