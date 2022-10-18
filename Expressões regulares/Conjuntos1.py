import re

# [arm] Retorna uma correspondência onde um dos caracteres especificados (a, r ou m) está presente
txt = "O calor do motor da moto"
#Verifique se a string tem algum a, r ou m caracteres:
x = re.findall("[arm]", txt)
# x = re.findall("[armOAb]", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# [a-m] Retorna uma correspondência para qualquer caractere minúsculo, em ordem alfabética entre a e m
txt = "O calor do motor da moto"
#Verifique se a string possui algum caractere entre a e m:
x = re.findall("[a-m]", txt)
# x = re.findall("[A-M]", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")