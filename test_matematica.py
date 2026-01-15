import pytest
from matematica import suma, resta
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 4) == -4

@pytest.mark.parametrize("a, b, resultado", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
]) 

def test_suma_param(a, b, resultado):
    assert suma(a, b) == resultado