import pytest

from calculator_logic import add, subtract, multiply, divide


def test_add_basic():
    assert add(5, 3) == 8


def test_subtract_basic():
    assert subtract(10, 4) == 6


def test_multiply_basic():
    assert multiply(6, 7) == 42


def test_divide_basic():
    assert divide(8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(9, 0)


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_divide_decimal_result():
    assert divide(5.5, 2) == pytest.approx(2.75)


def test_multiply_large_numbers():
    assert multiply(1_000_000, 3) == 3_000_000
