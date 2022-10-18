nomes = ["Robson", "Gabriel", "Danny", "Gustavo", "João", "Antonio"]
print(nomes)
#Remover item
nomes.remove("Danny")
print(nomes)
#Remove um item porem expecificando o idice
# Se não expecificar ele sempre vai remover o ultimo
nomes.pop(2)
print(nomes)

#Remove com idice tambem
del nomes[3]
print(nomes)

#Remove todos itens, mas a lista fica na memoria
nomes.clear()
#Apagar a lista toda
del nomes

print(nomes)
