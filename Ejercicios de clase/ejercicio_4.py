#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from poo1 import Alumno

from random import choice

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
calificacionesLista = []
becarios = [
    'Abaustista Erick',
    'Anaya Pérez Ulises Josué',
    'Bautista Parra Jonathan',
    'Castro Rendón Diego',
    'Castro Sierra Etni Sarai',
    'Chavez Bolaños Gustavo',
    'Cornejo de la Mora Iñaki',
    'Cruz Hérnandez Víctor Emiliano',
    'Flores Cid Marco',
    'García Chavelas Jonás',
    'García Rosas Dicter Tadeo',
    'García Velasco Erick Iram',
    'Gónzalez Castro Diego Daniel',
    'Hernández Vela Daniel',
    'Isunza Álvarez Marcos Guillermo',
    'López Miranda Angel Mauricio',
    'López Prado Emiliano',
    'Monterrubio Acosta Demian Alejandro',
    'Navarro Santana Pablo César',
    'Ortíz Amaya Bruno Fernando',
    'Reyes López Eduardo Alfonso',
    'Reyes Trujillo Guadalupe',
    'Ríos Raúl', 
    'Trujillo Beltrán Zianya Nenetzi', 
    'Verano Peralta María Fernanda',
    'Vázquez Kuri Eduardo', 
    'Zurita León Dana Cecilia']

def califica():
    for i in range(0, len(becarios)):
        calificacionesLista.append(choice(calificaciones))
        i += 1

def creaListaBecarios():
    alumnos = []
    for nombre in becarios:
        becario = Alumno(nombre, choice(calificaciones))
        alumnos.append(becario)
    return alumnos

def printAlumnos(lista):
    for alumno in lista:
        print(alumno.nombre, alumno.calificacion)

alumnos = creaListaBecarios()
printAlumnos(alumnos)



'''
def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)




def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('%s tiene %s\n' % (alumno,calificacion_alumno[alumno]))


asigna_calificaciones()
imprime_calificaciones()

def tuplas():
    aprobados = ()
    reprobados = ()
    for alumno,calificacion in calificacion_alumno.items():
        if calificacion >= 8:
            aprobados += (alumno,)
        else:
            reprobados += (alumno,)

    return aprobados,reprobados



def promedio():
    return sum(calificacion_alumno.values())/len(calificacion_alumno)



def conjuntoCalificaciones():
    return set(calificacion_alumno.values())


alumnos = tuplas()
print("\nAprobados:")
print(alumnos[0])

print("\nReprobados:")
print(alumnos[1])

print("\nPromedio:")
print(promedio())

print("\n Calificaciones obtenidas:")
print(conjuntoCalificaciones())
'''