import pytest
from funciones import validar_suma, validar_division, validar_busqueda

def test_validar_suma():
    assert validar_suma([1, 2, 3]) == 6
    with pytest.raises(ValueError):
        validar_suma([1, "a", 3])

def test_validar_division():
    assert validar_division(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        validar_division(10, 0)

def test_validar_busqueda():
    assert validar_busqueda([1, 2, 3], 2) == "Elemento '2' encontrado en la lista"
    assert validar_busqueda([1, 2, 3], 5) == "Elemento '5' NO está en la lista"
