import os

os.system("clear")
#Para limpar a tela do console:
#Linux: clear
#Windons: cls



# Entrada de dados
num1 = input("Digite o primeiro valor: ");
num1 = int(num1);

num2 = input("Digite o segundo valor: ");
num2 = int(num2);

# Processamento
mult = num1 * num2;

# Saida da informação
print();
print("A multiplicação de", num1, "por", num2, "é", mult);