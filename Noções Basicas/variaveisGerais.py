# Variável Global
def myFunc():
    print("Python é incrível")

myFunc()

x = "incrível"
def myFunc():
    x = "fantastico"
    print("Python é " + x)

myFunc()

print("Você é " + x)

# Variável Local
def myFunc():
    # Definindo a variavel z, como global
    global z
    z = "Bem vindo ao curso! "
    x = "fantastico"
    print("Python é " + x)

myFunc()