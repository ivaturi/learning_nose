# testing doctest with --doctest-tests flag
from my_module.doctest import *

def test_doctest():
    """
    >>> "b" == "b"
    True

    >>> "B" == "c"
    False

    >>> multiply(1,2)
    2
    """
    assert multiply(12,12) == 144
