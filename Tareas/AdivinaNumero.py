import datetime

def generaNumero():
    '''
    Genera un número entre 0 y 100
    :returns: int
    '''
    hora = datetime.datetime.now().microsecond % 1000
    dia = datetime.datetime.now().day
    return hora * dia % 100

def adivinaNumero():
    numeroCorrecto = generaNumero()
    print("Adivina el número entre 0 y 100, o escribe salir para salir")

    while True:

        numero = input()

        if numero == "salir":
            return
        
        if not numero.isdigit():
            print("Recuerda que es un número")
            continue

        if(int(numero) == numeroCorrecto):
            print("Coorrecto")
            return
        
        if(int(numero) < numeroCorrecto):
            print("Es mayor")
            pass
        
        if(int(numero) > numeroCorrecto):
            print("Es menor")
            pass


adivinaNumero()