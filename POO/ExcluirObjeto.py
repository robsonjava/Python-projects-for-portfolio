class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def myFunc(self):
        print("Olá meu nome é " + self.nome)

p1 = Pessoa("Robson", 30)
print("Nome: ", + p1.nome)
print("Idade: ", + p1.idade)

# Excluir objeto
del p1.idade
print("Nome: ", + p1.nome)
print("Idade: ", + p1.idade)

del p1