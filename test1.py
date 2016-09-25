# http://ivory.idyll.org/articles/nose-intro.html

"""
Most tests should take one of the following forms.
Either as a test method, or as a class that contains
several test methods 
"""

# basic testing
# nose looks for 'test_' methods, and runs them
def test_func():
    assert 'b' == 'b'


# a slightly more complicated example:
#
# In this case, nose will create an instance of TestExample,
# and only then run the test_c function
class TestExample:
    def test_c(self):
        assert 'c' == 'c'

"""
This is a common test pattern:
"""
