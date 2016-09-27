"""
Nose has support for the setup and teardown fixtures.
If the setup and teardown methods are defined, nose runs the setup
method before running anything else in the file, and the teardown
method after runnin everything else in the file. 

We can define things that need t be done before and after testing into
these methods.

Import:
from nose import with_setup 

Syntax:
For standalone methods, 

    def setup_module(module)
        <pre-testing stuff here>
        ...
        

    def teardown_module(module)
        <post-testing stuff here>
        ...


"""
from nose.plugins.attrib import attr
from modules.mathtools import *

def setup_module(mathtools):
    global a,b
    a = 5
    b = 10

def teardown_module(mathtools):
    pass

@attr(type="setup")
def test_setup_multiply():
    assert multiply(a,b) == 50
