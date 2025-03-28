"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    no_numeros = [x for x in lista if isinstance(x, str)]
    numeros = [x for x in lista if isinstance(x, (int, float))]
    lista[:] = no_numeros + numeros
    return lista
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    lista[:] = [x for x in lista if isinstance(x, str)] + [x for x in lista if isinstance(x, (int, float))]
    return lista
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    lista[:] = sorted(lista, key=lambda x: isinstance(x, (int, float)))
    return lista
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    no_numeros = list(filter(lambda x: isinstance(x, str), lista))
    numeros = list(filter(lambda x: isinstance(x, (int, float)), lista))
    lista[:] = no_numeros + numeros
    return lista
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    if not lista:  # Caso base: si la lista está vacía, devolverla
        return []
    if isinstance(lista[0], str):  # Si el primer elemento es una cadena
        return [lista[0]] + numeros_al_final_recursivo(lista[1:])
    else:  # Si el primer elemento es un número
        return numeros_al_final_recursivo(lista[1:]) + [lista[0]]
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
