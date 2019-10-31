'''
A collection of functions for DS8-Unit3-Sprint1
'''

import pandas
import numpy as np


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
    size_v = round(val_size * len(df))
    val = initial.sample(size_v)
    train = initial.drop(val.index)
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


def iqr_outliers(x, constant=1.5):
    '''
    A function to find and remove outliers from a given list
    Prints outliers and returns sorted new list without outliers
    '''
    a = np.array(x)
    # Sort list
    a.sort()
    # Get third quartile
    third = np.percentile(a, 75)
    # Get first quartile
    first = np.percentile(a, 25)
    # Get interquartile range (iqr)
    iqr = (third - first) * constant
    # Create set of first and third quartiles
    quart_set = (first - iqr, third + iqr)
    # Create new list for return
    new = []
    for i in a.tolist():
        # If item is outside of lower bound print
        if i <= quart_set[0]:
            print(f'{i} is a low outlier')
        # If item is outside of upper bount print
        elif i >= quart_set[1]:
            print(f'{i} is a high outlier')
        # If item is within bounds, append to list
        else:
            new.append(i)
    print('List without outliers:')
    return new
