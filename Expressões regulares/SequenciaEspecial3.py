import re

# \s Retorna uma correspondência onde a string contém um caractere de espaço em branco "\s"
txt = "O calor do motor da moto"
#Retorne uma correspondência para cada caractere de espaço em branco:
x = re.findall("\s", txt)
print(x)
if x:
	print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# \S Retorna uma correspondência onde a string NÃO contém um caractere de espaço em branco "\S"
txt = "O calor do motor da moto"
#Retorne uma correspondência para cada caractere de NÃO espaço em branco:
x = re.findall("\S", txt)
print(x)
if x:
	print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")