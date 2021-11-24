from calculator import Calculator


def test_multiply_success():
    cal = Calculator()
    assert cal.multiply(3, 3) == 9


def test_multiply_fail():
    cal = Calculator()
    assert cal.multiply(4, 3) != 9


def test_adding_success():
    cal = Calculator()
    assert cal.adding(3, 3) == 6


def test_adding_fail():
    cal = Calculator()
    assert cal.adding(4, 3) != 11


def test_division_success():
    cal = Calculator()
    assert cal.division(3, 3) == 1


def test_division_fail():
    cal = Calculator()
    assert cal.division(6, 3) != 5


def test_division_fail_null():
    cal = Calculator()
    assert cal.division(0, 3) != 5


def test_subtraction_success():
    cal = Calculator()
    assert cal.subtraction(33, 3) == 30


def test_subtraction_fail():
    cal = Calculator()
    assert cal.subtraction(4, 3) != 2
