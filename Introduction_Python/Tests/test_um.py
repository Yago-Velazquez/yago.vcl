from Introduction_Python.L7_Regular_Expressions.PS7.um import count

def test_1():
    assert count("Hello, um, i am pepe") == 1

def test_2():
    assert count("yummy") == 0

def test_3():
    assert count("um... i am um your father") == 2

def test_4():
    assert count("cat") == 0