def analizarTexto(cadena):

    cadena = cadena.lower()
    cadena = cadena.replace(',', '')
    cadena = cadena.replace('.', '')

    numeroPalabras = len(cadena.split(' '))

    numeroCaracetres = len(cadena.replace(' ', ''))

    aparicionesPalabras = {}

    for palabra in cadena.split(' '):
        if palabra in aparicionesPalabras:
            aparicionesPalabras[palabra] += 1
        else:
            aparicionesPalabras[palabra] = 1
    
    palabraComun = obtenerPorValor(aparicionesPalabras, max(aparicionesPalabras.values()))

    print('Número de palabras: ' + str(numeroPalabras))
    print('Número de caracteres: ' + str(numeroCaracetres))
    print('Apariciones de palabras: ' + str(aparicionesPalabras))
    print('Palabra más común: ' + palabraComun)
    


def obtenerPorValor (diccionario, valor):
    for clave in diccionario:
        if diccionario[clave] == valor:
            return clave
    return None


analizarTexto('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')


