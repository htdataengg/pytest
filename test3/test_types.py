from pytest import approx

def test_1():
    assert 1 == 1 # int
    assert "A" == "A" # str
    assert 1.0 == 1.0 # float
    assert [1, 2] == [1, 2] # array
    assert {"a":1} =={"a":1}  # json
    assert (0.1 + 0.2) == approx(0.3) # approx for floating point calculations
