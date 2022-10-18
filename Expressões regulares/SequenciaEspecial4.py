import re

# \w Retorna uma correspondência em que a string contém quaisquer caracteres de palavra (caracteres de a a Z, dígitos de 0-9 e o caractere sublinhado _) "\w"
txt = "O calor do motor 2021 da moto @%$#"
#Retorna uma correspondência para cada caractere de palavra (caracteres de a a Z, dígitos de 0-9 e o caractere sublinhado _):
x = re.findall("\w", txt)
print(x)
if x:
	print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# \W Retorna uma correspondência em que a string NÃO contém nenhum caractere de palavra "\W"
txt = "O calor do motor 2021 da moto @%$#"
#Retorne uma correspondência para cada caractere NÃO de palavra (caracteres NÃO entre a e Z. Como "!", "?" Espaço em branco etc.):
x = re.findall("\W", txt)
print(x)
if x:
	print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# \Z Retorna uma correspondência se os caracteres especificados estiverem no final da string "moto\Z"
txt = "O calor do motor da moto"
#Verifique se a string termina com "moto":
x = re.findall("moto\Z", txt)
print(x)
if x:
	print("Sim, há uma correspondência!")
else:
    print("Sem correspondência")