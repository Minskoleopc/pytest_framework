import pytest
import math
def test_sqrt():
    num = 25
    assert 25 == num

def testsquare():
    num = 7
    assert math.sqrt(7) == 4

@pytest.mark.smoke
def testEqual():
    assert 10 == 11

