import pytest
from app.calculations import add,substract,multiply,division


@pytest.mark.parametrize("num1,num2,expected",[(1,2,3),(3,4,7)])
def test_add(num1,num2,expected):
    assert add(num1,num2) == expected

def test_sub():
    assert substract(1,2) == -1
    
def test_multi():
    assert multiply(1,2) == 2

def test_divi():
    assert division(1,2) == 1
