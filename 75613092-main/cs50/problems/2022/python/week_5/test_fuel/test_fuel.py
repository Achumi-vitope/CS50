from fuel import gauge, convert
from pytest import raises

def test_one():
    with raises(ValueError):
        convert("cat/cat")
    with raises(ZeroDivisionError):
        convert("1/0")
    assert convert("50/100") == 50


def test_two():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

