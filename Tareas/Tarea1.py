def palindromoMasGrande(cadena):
    '''
    método que encuentra el palíndromo más grande en una cadena
    :params: cadena: str
    :returns: str
    '''
    cadena = cadena.lower()
    cadena = cadena.replace(' ', '')
    
    max_length = 0
    start = 0
    longitud = len(cadena)

    for i in range(longitud):
        for j in range(i, longitud):
            substring = cadena[i:j+1]
            if substring == substring[::-1]: 
                if max_length < len(substring):
                    start = i
                    max_length = len(substring)
    
    return cadena[start:start + max_length]

def esPrimo(numero):
    '''
    Método para deteminar si un número es primo
    :params: numero: int
    :returns: bool
    '''
    if numero <= 1:
        return False
    for i in range(2, numero-1):
        if numero % i == 0:
            return False
    return True

def primerosNPrimos(n, lista = [], i = 2):
    '''
    Método que encuentra los primeros n números primos de manera recursiva. Utiliza la función esPrimo
    :params: n: int, lista: list, i: int
    :returns: list
    '''
    if len(lista) < n:
        if esPrimo(i):
            lista.append(i)
            return primerosNPrimos(n, lista, i + 1)
        else:
            return primerosNPrimos(n, lista, i + 1)
    else:
        return lista

        

print(palindromoMasGrande('liaalaaiy'))

print(esPrimo(4))

print(primerosNPrimos(6))