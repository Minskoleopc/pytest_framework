import pytest
# Basic assertion
def test_basic_assertion():
    assert 5 == 6 # number
    assert "chinmay" == "satish" # string
    assert 10 > 5 # boolean assertion

# Comparing values assertion 
def test_number_assertions():
    assert 100 > 50
    assert 10 != 5
    assert 5 + 5 == 10

# String 
def test_number_assertions():
    assert "pytest" == "pytest"
    assert "pytest" != "pytest"

#Checking membership assetions(in, not in)
def test_list_membership():
    fruits = ["apple","mango","banana","orange"]
    assert "apple" in fruits # pass
    assert "grapes" not in fruits #pass

# String mememership
# one testcase can have multiple assertions
def test_string_membership():
    message ='hello i am learning , pytest'
    assert "welcome" in message
    assert "python" not in message

# Boolean assertions
def test_boolean_checks():
    assert 2 == 2 is True
    assert 3 == 4 is False 
    assert None is None

# Exception 
def divide(x,y):
    return x /y

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

# Custom assertion messages 
def test_custom_error():
    value = 5
    assert value == 10 ,f"Expected 10 but got {value}"