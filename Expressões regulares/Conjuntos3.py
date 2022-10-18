import re

# [0-9] Retorna uma correspondência para qualquer dígito entre 0 e 9
txt = "8 vezes antes de 11h45"
# Verifique se a string tem algum dígito:
x = re.findall("[0-9]", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# [0-5][0-9] Retorna uma correspondência para qualquer número de dois dígitos de 00 e 59
txt = "8 vezes antes de 11h45"
# Verifique se a string tem algum número de dois dígitos, de 00 a 59:
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")