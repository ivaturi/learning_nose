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
Basics of unit testing
-----------------------------------

This is a common test pattern:

def test():
    setup_test()
    try:
        do_test()
        make_test_assertions()
    finally:
        cleanup_after_test()


setup_test():
    Creates necessary objects, sets up database connections, find files,etc.
    (basically, sets up everything that is required to run the test)


do_test(), make_test_assertions():
    Actually run the test

cleanup_test_code():
    Regardless of status of the test, cleans up or tears down the preconditions


Fixtures
---------

Usually, frameworks provide for setting and tearing down preconditions,like so:

test.setUp = set_up_test
test.tearDown = cleanup_after_test

def test():
    do_test()
    make_test_assertions()

"""
