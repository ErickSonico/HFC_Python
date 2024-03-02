print(dict([(numero, (bin(numero)[2:], hex(numero)[2:])) for numero in range(1, 51) if bin(numero).count('1') % 2 != 0]))


