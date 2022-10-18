from distutils.command.clean import clean
import os
from turtle import clear

os.system("clear")
nomes = ["Robson", "Gabriel", "Danny", "Gustavo", "João", "Antonio"]
print(nomes)
#Alterando item
nomes[1] = "Danielle"
print(nomes)

#Alterando itens
nomes[1:3] = ["Gloria", "Beatriz"]
print(nomes)

#Inserindo item sem alterar a lista, colocando na ultima posição
nomes[1:3] = ["Gloria", "Beatriz","Flávio", "Lucas"]
print(nomes)