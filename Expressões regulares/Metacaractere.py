import re
# [] Um conjunto de caracteres "[a-m]"

txt = "O calor do motor da Moto"
# Caracteres minusculo em ordem alfabetica
x = re.findall("[a-m]", txt)
print(x)

# \ Sinaliza uma sequencia especial (também pode ser usado para caracteres de escape) "\d"

t = "Eu tenho 36 anos de idade"
y = re.findall("\d", t)
print(y)

# . Qualquer caractere (exceto caractere de nova linha) "mu..o"

z = "Olá Mundo!"
# Procure uma sequencia que comece com "mu", seguindo por dois (quaisquer) caracteres e um "o":
a = re.findall("Mu..o", z)
print(a)