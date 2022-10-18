import re

# ^	Começa com	"^Ola"
txt = "Ola mundo"
#Verifique se a string começa com 'Ola':
x = re.findall("^Ola", txt)
if x:
    print("Sim, a string começa com 'Ola'")
else:
    print("Sem correspondência")

# $	Acaba/Termina com "mundo$"
txt = "Ola mundo"
#Verifique se a string termina com 'mundo':
x = re.findall("mundo$", txt)
if x:
    print("Sim, a string termina com 'mundo'")
else:
    print("Sem correspondência")

# *	Zero ou mais ocorrências "orx*"
txt = "O calor do motor da moto."
#Verifique se a string contém "or" seguido por 0 ou mais caracteres "x":
x = re.findall("orx*", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")