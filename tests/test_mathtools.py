# testing doctest with --doctest-tests flag
from modules.mathtools  import *

def test_tests_within_comments():
    """
    >>> "B" == "c"
    False
    """
    assert multiply(12,12) == 144


def test_factorial():
    assert factorial(5) == 5*4*3*2*1
    assert factorial(3) == 3*2*1
    assert factorial(10) == 10*9*8*7*6*5*4*3*2*1
    assert not factorial(12) == 1

def test_fibonacci():
    assert fibonacci(3) == [1,2,3]
    assert fibonacci(5) == [1,2,3,5,8]
    assert fibonacci(8) == [1,2,3,5,8,13,21,34]
    assert fibonacci(1) == [1]
    assert fibonacci(2) == [1,2]
