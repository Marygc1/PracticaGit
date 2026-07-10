def validar_suma(lista):
    """Suma los elementos de una lista, validando que sean números"""
    if not all(isinstance(x, (int, float)) for x in lista):
        raise ValueError("La lista contiene elementos no numéricos")
    return sum(lista)


def validar_division(dividendo, divisor):
    """Divide dos números, validando divisor distinto de cero"""
    if not isinstance(dividendo, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Ambos valores deben ser numéricos")
    if divisor == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return dividendo / divisor


def validar_busqueda(lista, elemento):
    """Busca un elemento en la lista, validando que exista"""
    if elemento in lista:
        return f"Elemento '{elemento}' encontrado en la lista"
    else:
        return f"Elemento '{elemento}' NO está en la lista"
