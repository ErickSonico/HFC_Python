import re

# sub para sustituir patrones
# sub(patron, nuevo, cadena)
# search para buscar patrones 
# match para buscar patrones al principio de la cadena


patron = r"[A-Za-z]{4}[0-9]{4}"
patron2 = r"[^$]+\$"
patron3 = r"\/\*[\s\S]\*\/"
patron4 = r"[A-Za-z]\w*"
patron5 = r"[a-z0-9.-_]+@ciencias\.unam\.mx$"
patron6 = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
patron7 = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


