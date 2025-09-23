import pytest
from Introduction_Python.L5_Unit_tests.PS5.twitter import shorten


def test_greeting():
    assert shorten("Hello, world") == "Hll, wrld"

def test_number():
    with pytest.raises(TypeError):
        shorten(4546)

def test_empty():
    assert shorten() == "Hll, wrld"