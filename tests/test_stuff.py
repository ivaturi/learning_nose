# testing doctest with --doctest-tests flag
from modules.mathtools  import *

def test_doctest():
    """
    >>> "B" == "c"
    False
    """
    assert multiply(12,12) == 144
