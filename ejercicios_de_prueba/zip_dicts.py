lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3, 4, 5]

print(dict(zip(lista1, lista2)))
print(list(map(lambda x: 2 * x, lista2)))
print(list(filter(lambda x : x % 2 == 0, lista2)))
