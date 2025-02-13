import pytest
import math
def test_sqrt2():
    num = 25
    assert 25 == num

@pytest.mark.xfail(reason="The dom is updated")
@pytest.mark.login
def testsquare2():
    num = 7
    assert math.sqrt(7) == 49

@pytest.mark.smoke
def testEqual2():
    assert 10 == 10
