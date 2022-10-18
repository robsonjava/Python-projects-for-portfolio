from audioop import reverse

nomes = ["Robson", "Gabriel", "Danny", "Gustavo", "João", "Antonio"]
numeros = [100, 50, 65, 82, 23]

#Ordem em alfabedo e cresente
nomes.sort()
numeros.sort()

def myfunction(n):
    return abs(n-50)

numeros.sort(key = myfunction)

nomes.sort(reverse = True)
numeros.sort(reverse = True)



print(nomes)
print(numeros)