import re

# [^arm] Retorna uma correspondência para qualquer caractere EXCETO a, r e m
txt = "O calor do motor da moto"
#Verifique se a string possui outros caracteres além de a, r ou m:
x = re.findall("[^arm]", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# [0123] Retorna uma correspondência onde qualquer um dos dígitos especificados (0, 1, 2 ou 3) estão presentes
txt = "O calor do motor 1985 da moto"
# Verifique se a string tem dígitos  0, 1, 2 ou 3:
x = re.findall("[0123]", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")