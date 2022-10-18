# CRIAR UM ARQUIVO NOVO
#f = open("texto1.txt", "x")

# LER UM ARQUIVO
#f = open("texto1.txt", "r")

# GRAVAR UM ARQUIVO
#f = open("texto1.txt", "w")

# ANEXAR UM ARQUIVO
#f = open("texto1.txt", "a")


f = open("texto1.txt", "a")
f.write("Agora o arquivo tem conteudo.\nAgora o arquivo tem conteudo.")
f.close

f = open("texto1.txt", "r")
print(f.read())
f.close