import os
import shutil

# Saber se o arquivo existe primeiro
if os.path.exists("texto.txt"):
    os.remove("texto.txt")
else:
    print("Não existe!")

# Remover pasta
if os.rmdir("Nome da pasta"):

# Modulo shutil
shutil.rmtree("Nome da pasta")