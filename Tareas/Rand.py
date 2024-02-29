import random


def generadorContraseña(minusculas, mayusculas, digitos, contraseña = ""):
    '''
    Método que genera contraseñas seguras y aleatorias
    :params: minusculas: int, mayusculas: int, digitos: int
    :returns: str
    '''
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    abecedarioMayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caracter = random.randint(1,3)

    if minusculas == 0 and mayusculas == 0 and digitos == 0:
        return contraseña
    
    if caracter == 1 and minusculas > 0: 
        contraseña += abecedario[random.randint(0,25)]
        return generadorContraseña(minusculas - 1, mayusculas, digitos, contraseña)

    if caracter == 2 and mayusculas > 0: 
        contraseña += abecedarioMayusculas[random.randint(0,25)]
        return generadorContraseña(minusculas, mayusculas - 1, digitos, contraseña)

    if caracter == 3 and digitos > 0:  
        contraseña += str(random.randint(0,9))
        return generadorContraseña(minusculas, mayusculas, digitos - 1, contraseña)
    
    return generadorContraseña(minusculas, mayusculas, digitos, contraseña)


print('Contraseña: ' + generadorContraseña(8, 8, 8))