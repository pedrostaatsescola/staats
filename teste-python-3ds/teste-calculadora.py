# test_calculadora.py
import pytest
from calculadora import soma, subtrai, multiplica, divide

@pytest.mark.parametrize("a, b, esperado", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -1, -2)
])
def test_soma(a, b, esperado):
    assert soma(a, b) == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (10, 5, 5),
    (-1, -1, 0),
    (0, 1, -1)
])
def test_subtrai(a, b, esperado):
    assert subtrai(a, b) == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (3, 7, 21),
    (-1, 1, -1),
    (0, 10, 0)
])
def test_multiplica(a, b, esperado):
    assert multiplica(a, b) == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (10, 2, 5),
    (-10, 2, -5)
])
def test_divide(a, b, esperado):
    assert divide(a, b) == esperado

def test_divide_por_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
