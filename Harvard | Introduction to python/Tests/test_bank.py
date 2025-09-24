import pytest
from Introduction_Python.L5_Unit_tests.PS5.banks import value

def test_hello():
    assert value("hi") == 20

def test_number():
    with pytest.raises(AttributeError):
        value(676)