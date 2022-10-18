import re

# \A Retorna uma correspondência se os caracteres especificados estiverem no início da string
txt = "Ola Mundo"
#Verifique se a string começa com "Ola":
x = re.findall("\AOla", txt)
print(x)
if x:
    print("Sim, há uma correspondência!")
else:
    print("Sem correspondência")

# \b Retorna uma correspondência onde os caracteres especificados estão no início ou no final de uma palavra
# (o "r" no início está garantindo que a string está sendo tratada como uma "string bruta") r"\btor", r"tor\b"
txt = "O calor do motor da moto"
#Verifique se "tor" está presente no início de uma PALAVRA:
x = re.findall(r"\btor", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")
#Verifique se "tor" está presente no final de uma PALAVRA:
x = re.findall(r"tor\b", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")
