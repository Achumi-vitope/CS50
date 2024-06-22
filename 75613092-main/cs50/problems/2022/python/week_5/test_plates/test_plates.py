from plates import is_valid


def test_one():
    assert is_valid("cs50") == True
    assert is_valid("cs5067") == True


def test_two():
    assert is_valid("69") == False
    assert is_valid("c") == False

def test_three():
    assert is_valid("cs0689") == False
    assert is_valid("cs50h9") == False

def test_four():
    assert is_valid("cs5067890") == False
    assert is_valid("PI3.14") == False