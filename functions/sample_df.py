import pandas as pd
# Sample DataFrame to use for testing functions
columns = ['Year', 'Name', 'YearName', 'College', 'POS', 'Height',
           'Weight', 'Hand Size', 'Arm Length', 'Wonderlic',
           '40 Yard', 'Bench Press', 'Vert Leap', 'Broad Jump',
           'Shuttle', '3Cone', '60Yd Shuttle', 'Pick', 'Round']
datapath = r'C:\Users\Nick\Unit2Project\Attempt 2\Data'
df = pd.read_csv(datapath + r'\NFLCombineData.csv', names=columns).drop(0)
