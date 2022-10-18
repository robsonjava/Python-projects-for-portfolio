x = "Olá Mundo!"
try:
    print(x)
except NameError:
    print("Variavel x não definida")

except:
    print("Aconteceu uma exceção")

else:
    print("Tudo certo por aqui!")
finally:
    print("O try except foi finalizado")

print("Continuando o programa.")