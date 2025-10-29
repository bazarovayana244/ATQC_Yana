import pytest
from calculator_client import CalculatorClient

@pytest.fixture(scope="module")
def calculator():
    return CalculatorClient()

def test_add(calculator):
    result = calculator.add(25, 48)
    assert result == 73

def test_subtract(calculator):
    result = calculator.subtract(48, 1)
    assert result == 47

def test_multiply(calculator):
    result = calculator.multiply(5, 8)
    assert result == 40

def test_divide(calculator):
    result = calculator.divide(125, 5)
    assert result == 25

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="SOAP Fault"):
        calculator.divide(5, 0)