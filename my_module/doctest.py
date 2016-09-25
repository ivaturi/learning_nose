
# Testing docstrings
"""
nose can detect and run doctests.
to use this, however, the tests to be run must be part of a package
as a module.
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
