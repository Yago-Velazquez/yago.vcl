from Introduction_Python.L7_Regular_Expressions.PS7.numb3rs import validate

def test_standard():
    assert validate("255.255.255.255") == True

def test_large():
    assert validate("345.4.5.6") == None

def test_toomany():
    assert validate("1.1.1.1.1") == None

def test_toofew():
    assert validate("1.1.1") == None

def test_string():
    assert validate("cat") == None