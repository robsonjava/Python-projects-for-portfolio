#Uma funcao recusiva é uma funcao que chama ela mesma dentro do seu proprio bloco

# Sem recusividade
def repetir(n):
    for x in range(n):
        print("Olá Mundo!")

repetir(4)


# Com recusividade
def repetirRecursivo(n):
    if n > 0:
        print("Olá Mundo Recursivo!")
        repetirRecursivo(n-1)

repetirRecursivo(3)