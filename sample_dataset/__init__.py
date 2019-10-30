'''
A sample dataset to use with functions in nckflannery
'''
import os
from os.path import dirname, join
import pandas as pd


def load_NFL_data():
    module_path = dirname(__file__)
    file_path = join(module_path, 'data', 'NFLCombineData.csv')
    columns = ['Year', 'Name', 'YearName', 'College', 'POS', 'Height',
               'Weight', 'Hand Size', 'Arm Length', 'Wonderlic',
               '40 Yard', 'Bench Press', 'Vert Leap', 'Broad Jump',
               'Shuttle', '3Cone', '60Yd Shuttle', 'Pick', 'Round']
    x = pd.read_csv(file_path, names=columns).drop(0)
    return x
