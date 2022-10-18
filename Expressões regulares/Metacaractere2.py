import re

# + Uma ou mais ocorrências "orx+"
txt = "O calor do motor da moto."
# Verifique se a string contém "or" seguido por 1 ou mais caracteres "x"
x = re.findall("orx+", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# {} Exatamente o número especificado de ocorrências "al{2}"
txt = "O calor do motor da moto."
#Verifique se a string contém "m" seguido por exatamente dois caracteres "o":
x = re.findall("mo{1}", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# | Ou "cai|permanece"
txt = "A chuva na Espanha cai principalmente na planície!"
#Verifique se a string contém "cai" ou "permanece":
x = re.findall("cai|permanece", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")