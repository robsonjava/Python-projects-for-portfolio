class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def myFunc(self):
        print("Olá meu nome é " + self.nome)

p1 = Pessoa("Robson", 30)
p1.myFunc()

p2 = Pessoa("Alexandra", 35)
p2.myFunc()