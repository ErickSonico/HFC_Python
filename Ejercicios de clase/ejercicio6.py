#!/usr/bin/python
#HACKERS_FIGHT_CLUB

simpsons = ['homero','lisa','bart']
pokemon = ['ash','brock','misty']
rickymorty = ['rick','morty','jerry','squanchy']
malcom = ['dewey','reese','hal','lois','francis','malcom']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION

print((lambda x: [elem.upper() for elem in x if 'i' in elem])((lambda w,x,y,z : w + x + y + z)(simpsons, pokemon, rickymorty, malcom)))