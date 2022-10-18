set1 = {"Gabriel", "Danny", "Arthur", "Robson"}
set2 = {"Guilherme", "Danilo", "Alfredo", "Rodrigo", "Danny"}

#Modo 01
#set1.update(set2)
#print(set1)

#Modo 02
#set3 = set1.union(set2)
#print(set3)

#Interseção Mantem somente o item duplicado
set1.intersection_update(set2)
print(set1)

#Duplicado
set3 = set.intersection(set2)
print(set3)

#Mater todos menos os duplicados
set1.symmetric_difference_update(set2)
print(set1)

#Apenas os itens diferentes
set4 = set1.symmetric_difference(set2)
print(set4)