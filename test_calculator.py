import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator


def test_adding(calculator):
    assert calculator.add(2, 2) == 4


def test_substract(calculator):
    assert calculator.subtract(5,1) == 4


def test_multiply(calculator):
    assert calculator.multiply(5, 2) == 10


def test_divide(calculator):
    assert calculator.divide(12,2) == 6

