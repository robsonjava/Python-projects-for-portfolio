import re

# [a-zA-Z] Retorna uma correspondência para qualquer caractere alfabeticamente entre a e z, minúsculas OU maiúsculas
txt = "8 Vezes Antes de 11h45"
# Verifique se a string tem caracteres de a a z em minúsculas e de A a Z em maiúsculas:
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")

# [+] Em conjuntos, +, *,., |, (), $, {} Não tem nenhum significado especial, então [+] significa: retorna uma correspondência para qualquer caractere + na string
txt = "8 vezes antes de 11h45"
# Verifique se a string possui quaisquer caracteres +:
x = re.findall("[+]", txt)
print(x)
if x:
    print("Sim, há pelo menos uma correspondência!")
else:
    print("Sem correspondência")