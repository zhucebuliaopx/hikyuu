import pytest
import pickle
from hikyuu import Parameter


def test_Parameter():
    x = Parameter()
    assert x.have("1") == False

    x["1"] = True
    assert x.have("1") == True
    assert x['1'] == True

    x["1"] = False
    assert x['1'] == False

    with pytest.raises(RuntimeError):
        x['1'] = 1

    x['2'] = 10
    assert x['2'] == 10

    x['2'] = 30
    assert x['2'] == 30

    with pytest.raises(RuntimeError):
        x['2'] = True

    x['3'] = 3.1
    assert x['3'] == 3.1
    x['3'] = 5.3
    assert x['3'] == 5.3
    with pytest.raises(RuntimeError):
        x['3'] = 3

    x['4'] = '中国'
    assert x['4'] == '中国'
    x['4'] = 'test'
    assert x['4'] == 'test'
    with pytest.raises(RuntimeError):
        x['4'] = 1

    assert x.have('unsupport') == False
    with pytest.raises(RuntimeError):
        x['unsupport'] = []


def test_Parameter_pickle():
    x = Parameter()
    x['1'] = 2
    x['2'] = 3
    with open("temp", "wb") as f:
        pickle.dump(x, f)

    with open("temp", "rb") as f:
        d = pickle.load(f)

    assert d['1'] == 2
    assert d['2'] == 3