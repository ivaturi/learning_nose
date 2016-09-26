# testing doctest with --doctest-tests flag
from modules.mathtools  import *
from nose.plugins.attrib import attr

"""
attributes:
-----------
A test can be assigned attributes, which can be used as filters
when asking nose to selectively run tests, using the flag:

-a <FLAG>
(or)
-a !<FLAG>
"""
@attr(type='basic')
def test_tests_within_comments():
    """
    >>> "B" == "c"
    False
    """
    assert multiply(12,12) == 144


"""
To run only the tests tagged with type=math, use this:

> nosetests -v -a type=math

"""
@attr(type='math')
def test_factorial():
    assert factorial(5) == 5*4*3*2*1
    assert factorial(3) == 3*2*1
    assert factorial(10) == 10*9*8*7*6*5*4*3*2*1
    assert not factorial(12) == 1

@attr(type='math')
def test_fibonacci():
    assert fibonacci(5)  == [0,1,1,2,3]
    assert fibonacci(7)  == [0,1,1,2,3,5,8]
    assert fibonacci(10) == [0,1,1,2,3,5,8,13,21,34]
    assert fibonacci(0)  == []
    assert fibonacci(1)  == [0]
    assert fibonacci(2)  == [0,1]
    assert fibonacci(3)  == [0,1,1]


