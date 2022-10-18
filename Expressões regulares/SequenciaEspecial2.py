import re

# \B Retorna uma correspondência onde os caracteres especificados estão presentes, mas NÃO no início (ou no final) de uma palavra
# (o "r" no início está garantindo que a string está sendo tratada como uma "string bruta") r"\Btor", r"tor\B"]
txt = "O calor do motor da moto dos pastores"
#Verifique se "tor" está presente, mas NÃO no início de uma palavra:
# x = re.findall(r"\Btor", txt)
x = re.findall(r"tor\B", txt)
print(x)
if x:
	print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# \d Retorna uma correspondência onde a string contém dígitos (números de 0 a 9) "\d"
txt = "O calor do motor 2021 da moto"
#Verifique se a string contém algum dígito (números de 0 a 9):
x = re.findall("\d", txt)
print(x)
if x:
	print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# \D Retorna uma correspondência onde a string NÃO contém dígitos (números de 0 a 9) "\D"
txt = "O calor do motor 2021 da moto"
#Retorna uma correspondência a cada caractere sem dígitos:
x = re.findall("\D", txt)
print(x)
if x:
	print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")