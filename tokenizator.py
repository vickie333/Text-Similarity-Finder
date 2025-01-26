delimitadores = {" ", '(', ')', '[', ']', '{', '}', ',', ':', ';', '.',
                 '+', '-', '', '/', '%', '//', '*', '<', '>', '==', '!=',
                 '<=', '>=', '=', '&', '|', '^', '#', '\'', '"', '\\', '@', '$', '?', '!',
                 '\n', '\t', '\r', '`', '~'}

def token(cadena):
    """
    Tokeniza una cadena eliminando delimitadores y devolviendo una lista de tokens.

    Args:
        cadena (str): Cadena a tokenizar.

    Returns:
        list: Lista de tokens sin delimitadores.
    """
    result = []
    value = ""

    for char in cadena.lower():
        if char in delimitadores:
            if value:
                result.append(value)
                value = ""
        else:
            value += char
    if value:
        result.append(value)

    return result
