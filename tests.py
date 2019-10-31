''' Tests for all functions '''
import sample_dataset as sd
import nckflannery as nf
import pandas as pd


def test_load_data():
    assert sd.load_NFL_data()['Name'].iloc[0] == 'Ameer Abdullah'
    assert sd.load_NFL_data().shape == (9312, 19)


def test_is_null():
    a = pd.DataFrame([[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3]])
    assert (nf.is_null(a).loc[2] == (False, False, False, True, True)).tolist()

def test_split():
    df = sd.load_NFL_data()
    train, val, test = nf.train_val_test_split(df)
    assert train.shape == (5588, 19)
    assert val.shape == (1862, 19)
    assert test.shape == (1862, 19)

def test_iqr():
    a = [1,2,3,4,2000]
    b = [1,2,3,4,500000,9,-24, 42, 1000, -42, -5555, -2441,1]
    assert nf.iqr_outliers(a) == [1,2,3,4]
    assert nf.iqr_outliers(b) == [-42, -24, 1, 1, 2, 3, 4, 9, 42]