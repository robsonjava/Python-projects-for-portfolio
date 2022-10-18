f = open("texto.txt", "r", encoding="UTF-8")
#print(f.read())

# Ler uma linha
#print(f.readline())

for x in f:
    print(x)

# Fechar arquivo

f.close()