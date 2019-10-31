# Nckflannery_lambdata
A package of useful functions for Data Science  
Can be found at: https://test.pypi.org/project/Nckflannery-lambdata/  
Or `pip install -i https://test.pypi.org/simple/ Nckflannery-lambdata`  
Dependencies : `pandas numpy pytest`
# Modules:

## sample_dataset
Contains a function to load a sample dataset to work with  
**Example:**
```
>>> import sample_dataset as sd
>>> a = sd.load_NFL_data()
>>> a.head()
```
```
   Year               Name               YearName              College POS Height Weight Hand Size Arm Length Wonderlic 40 Yard Bench Press Vert Leap Broad Jump Shuttle 3Cone 60Yd Shuttle Pick Round
1  2015     Ameer Abdullah     2015Ameer Abdullah             Nebraska  RB  68.75    205      8.63         30       NaN     4.6          24      42.5        130    3.95  6.79        11.18   54     2
2  2015     Nelson Agholor     2015Nelson Agholor  Southern California  WR  72.13    198      9.25      32.25       NaN    4.42          12       NaN        NaN     NaN   NaN          NaN   20     1
3  2015      Malcolm Agnew      2015Malcolm Agnew    Southern Illinois  RB     70    202       NaN        NaN       NaN    4.59         NaN       NaN        NaN     NaN   NaN          NaN  NaN   NaN
4  2015          Jay Ajayi          2015Jay Ajayi          Boise State  RB  71.75    221        10         32        24    4.57          19        39        121     4.1   7.1         11.1  149     5
5  2015  Brandon Alexander  2015Brandon Alexander      Central Florida  FS     74    195       NaN        NaN       NaN    4.59         NaN       NaN        NaN     NaN   NaN          NaN  NaN   NaN
```
```
>>> a.shape
(9312, 19)
```
## nckflannery
### Contains Functions:

### **is_null**  
Takes dataframe and returns dataframe showing which items are null.  
**Example:**
```
>>> import nckflannery as nf
>>> nf.is_null(a).head()
```
```
Year   Name  YearName  College    POS  Height  Weight  Hand Size  Arm Length  Wonderlic  40 Yard  Bench Press  Vert Leap  Broad Jump  Shuttle  3Cone  60Yd Shuttle   Pick  Round
1  False  False     False    False  False   False   False      False       False       True    False        False      False       False    False  False         False  False  False
2  False  False     False    False  False   False   False      False       False       True    False        False       True        True     True   True          True  False  False
3  False  False     False    False  False   False   False       True        True       True    False         True       True        True     True   True          True   True   True
4  False  False     False    False  False   False   False      False       False      False    False        False      False       False    False  False         False  False  False
5  False  False     False    False  False   False   False       True        True       True    False         True       True        True     True   True          True   True   True
```
```
>>> nf.is_null(a, True)
Year               0
Name               0
YearName           0
College            0
POS                0
Height             0
Weight             0
Hand Size       1518
Arm Length      1836
Wonderlic       8960
40 Yard          750
Bench Press     3006
Vert Leap       1784
Broad Jump      1920
Shuttle         2598
3Cone           5186
60Yd Shuttle    6263
Pick            3599
Round           3599
dtype: int64
```

### train_val_test_split  
Takes dataframe and splits into three smaller dataframes for train/val/test.  
**Example:**
```
>>> a.shape
(9312, 19)
```
```
>>> train_a, val_a, test_a = nf.train_val_test_split(a, test_size=0.2, val_size=0.2)     
>>> train_a.shape, val_a.shape, test_a.shape
((5588, 19), (1862, 19), (1862, 19))
```
### iqr_outliers  
Function to find and remove outliers from a given list, then prints outliers 
and returns new sorted list  
**Example:**
```
>>> b = [1,2,3,4,200]
>>> nf.iqr_outliers(b)
200 is a high outlier
List without outliers:
[1, 2, 3, 4]
>>> c = [-20, 2424, 10, 1, 2, 3, 4, 5, 0] 
>>> nf.iqr_outliers(c)
-20 is a low outlier
2424 is a high outlier
List without outliers:
[0, 1, 2, 3, 4, 5, 10]
```


