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
