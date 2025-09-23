from Introduction_Python.L7_Regular_Expressions.PS7.working import convert, change_time, minutes
import sys

def test_standard():
    assert convert("10:35 AM to 9:45 PM") == "10:35 to 21:45"