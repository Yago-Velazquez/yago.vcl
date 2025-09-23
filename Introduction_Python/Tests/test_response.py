from Introduction_Python.L7_Regular_Expressions.PS7.response import validation


def test_emaiL():
    assert validation("yago.vcl@gmail.com") == True

def test_wrong():
    assert validation("cat") == False

def test_none():
    assert validation("") == False

def test_standard():
    assert validation("something@domain.tld") == True