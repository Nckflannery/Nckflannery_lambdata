'''
A collection of functions for DS8-Unit3-Sprint1
'''

import pandas as pd


def train_val_test_split(df, test_size=0.2, val_size=0.2):
    '''
    Returns three dataframes. First splits DF into initial/test
based on test_size, then splits initial into train/val based
on val_size.
df = Pandas DataFrame to split
test_size = Size (number of rows) of returned 'test' DataFrame
after split (default = 0.2)
val_size = Size (number of rows) of returned 'val' DataFrame
after split (default = 0.2)
Example: train, val, test = train_val_test_split(df = pd.DataFrame,
test_size = 0.3, val_size = 0.2)
    '''
    size_t = round(test_size * len(df))
    test = df.sample(size_t)
    initial = df.drop(test.index)
    size_v = round(val_size * len(initial))
    val = initial.sample(size_v)
    train = df.drop(val.index)
    return train, val, test


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
