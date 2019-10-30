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


def iqr_outliers(x):
    '''
    A function to find and remove outliers from a given list
    Prints outliers and returns new list
    '''
    # sort the function
    x.sort()
    # If list is too short
    if len(x) <= 3:
        print('List too small!')
    # If list is length 4
    elif len(x) == 4:
        first = x[0]
        third = x[2]
        # Get interquartile range
        iqr = third - first
        # Get 1.5*IQR below first quartile
        low = first - (1.5 * iqr)
        # Get 1.5*IQR above third quartile
        high = third + (1.5 * iqr)
        # Print which items are outliers
        # Create new list for return without outliers
        new = []
        for i in range(0, len(x)):
            if x[i] < low:
                print(f'{x[i]} is a low outlier')
            elif x[i] > high:
                print(f'{x[i]} is a high outlier')
            else:
                new.append(x[i])
        print('List without outliers:')
        return new
    else:
        # If list is even
        if len(x) % 2 == 0:
            # Get midpoint
            mid = round(len(x)/2)
            # Get first quartile
            first = (x[int(mid/2)] + x[int(mid/2)-1])/2
            # Get third quartile
            third = (x[len(x)-int(mid/2)] + x[len(x)-(int((mid-1)/2))])/2
        # If list is odd
        else:
            # Get midpoint
            mid = round((len(x)+1)/2)
            # Get first quartile
            first = x[int((mid-1)/2)]
            # Get third quartile
            third = x[len(x) - int((mid-1)/2)]
        # Get interquartile range
        iqr = third - first
        # Get 1.5*IQR below first quartile
        low = first - (1.5 * iqr)
        # Get 1.5*IQR above third quartile
        high = third + (1.5 * iqr)
        # Print which items are outliers
        # Create new list for return without outliers
        new = []
        for i in range(0, len(x)):
            if x[i] < low:
                print(f'{x[i]} is a low outlier')
            elif x[i] > high:
                print(f'{x[i]} is a high outlier')
            else:
                new.append(x[i])
        print('List without outliers:')
        return new
