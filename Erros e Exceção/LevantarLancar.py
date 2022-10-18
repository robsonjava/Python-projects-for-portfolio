x = 5

if x < 0:
    raise Exception("Não são permitidos números negativos")

y = 10

if not type(y) is int:
    raise TypeError("Somente números")

print("Fim do programa")