# Generador de contraseñas a partir de una lista de palabras en un archivo .txt

from random import choice, randint

digitos = '0123456789'
letras = 'abcdefghijklmnopqrstuvwxyz'
simbolos = '.,-_!#%&/=?*@'

def obten_palabras(archivo):
    '''
    Crea una lista de palabras a partir de un archivo .txt
    '''
    palabras = []
    with open(archivo, 'r') as lista:
        for line in lista.readlines():
            palabras.append(line)
    palabras = [palabra.replace('\n','') for palabra in palabras]
    return palabras

def reemplaza_letras_numeros(palabra):
    '''
    Reemplaza o no el caracter por una letra o número
    '''
    caracteres = [*palabra]
    for caracter in caracteres:
        num = randint(1,3)
        if num == 1:
            if caracter.isdigit():
                caracteres[caracteres.index(caracter)] = choice(letras)
            else:
                caracteres[caracteres.index(caracter)] = choice(digitos)
    return ''.join(caracteres)

def agrega_simobolos(palabra):
    '''
    Agrega caracetres especiales y números al inicio o final de la palabra
    '''
    for i in range(len(palabra)):
        num = randint(1,4)
        if num == 1:
            palabra = palabra + choice(digitos)
            i+=1
        if num == 2:
            palabra = choice(digitos) + palabra
            i+=1
        if num == 3:
            palabra = palabra + choice(simbolos)
            i+=1
        if num == 4:
            palabra = choice(simbolos) + palabra
            i+=1
    return palabra

def escribe_contraseñas(lista):
    '''
    Escribe la lista de contraseñas en un archivo .txt 
    '''
    with open('contraseñas.txt', 'w') as archivo:
        for contraseña in lista:
            archivo.write(contraseña + '\n')
    print('Se ha creado el archivo con contraseñas!')

    
def genera_contraseñas(archivo):
    '''
    Aplica los métodos anteriores para generar las contraseñas
    '''
    lista = obten_palabras(archivo)
    contraseñas = [reemplaza_letras_numeros(elem) for elem in lista]
    contraseñas = [agrega_simobolos(elem) for elem in contraseñas]
    contraseñas = [elem[::-1] for elem in contraseñas]
    escribe_contraseñas(contraseñas)

genera_contraseñas('palabras.txt')
    

