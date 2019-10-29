import pandas as pd


def sample_df():
    # Sample DataFrame to use for testing functions
    columns = ['Year', 'Name', 'YearName', 'College', 'POS', 'Height',
               'Weight', 'Hand Size', 'Arm Length', 'Wonderlic',
               '40 Yard', 'Bench Press', 'Vert Leap', 'Broad Jump',
               'Shuttle', '3Cone', '60Yd Shuttle', 'Pick', 'Round']
    df = pd.read_csv('sample_data\\NFLCombineData.csv', names=columns).drop(0)
    return df
