"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    return palabra == palabra[::-1]
    pass # Completar


# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    c = (len(palabra)+1)//2
    return palabra[:c]
    pass # Completar


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
