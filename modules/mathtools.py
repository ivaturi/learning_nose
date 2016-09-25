

"""
> Testing docstrings
--------------------
nose can detect and run doctests.
to use this, however, the tests to be run must be part of a package
as a module.

To run nose with doctests, use the flag

    --with-doctest 


By default, nose only looks for doctests in non-test code.
nose can be configured to look for doctests in test code too, with the flag

    --doctest-tests

"""

def multiply(a,b):
    """
    Multiplies two numbers
    
    nose will execute all the lines that begin with '>>>'
    
    >>> multiply(5,10)
    50

    >>> multiply(0,10)
    0
    
    >>> multiply(0.5, 30)
    15.0
    """
    return a*b


def add(a,b):
    return a+b

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
