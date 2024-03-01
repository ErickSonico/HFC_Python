print((lambda x, y, z : x * y * z)(100, 8, 3.14159))

print((lambda lista : len(lista) == 0)([]))
print((lambda lista : len(lista) == 0)([1,2]))

print((lambda lista, n: len(lista) >= n)([1,2,3], 2))

print((lambda n: n ** 0.5)(2))

print((lambda conjunto1, conjunto2: conjunto1.intersection(conjunto2))({1,2,3}, {3,4,5}))