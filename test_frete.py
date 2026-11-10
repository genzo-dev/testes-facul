import pytest

from frete import calcular_frete


def test_frete_produto_500g():
    assert calcular_frete(500) == 10


def test_frete_produto_2000g():
    assert calcular_frete(2000) == 20


def test_frete_produto_6000g():
    assert calcular_frete(6000) == 30


def test_frete_peso_1g():
    assert calcular_frete(1) == 10


def test_frete_peso_1000g():
    assert calcular_frete(1000) == 10


def test_frete_peso_1001g():
    assert calcular_frete(1001) == 20


def test_frete_peso_5000g():
    assert calcular_frete(5000) == 20


def test_frete_peso_5001g():
    assert calcular_frete(5001) == 30


def test_frete_peso_zero():
    with pytest.raises(ValueError):
        calcular_frete(0)


def test_frete_peso_negativo():
    with pytest.raises(ValueError):
        calcular_frete(-1)
