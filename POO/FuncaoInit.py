class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Robson", 30)
print(p1.nome)
print(p1.idade)

p2 = Pessoa("Danny", 35)
print(p2.nome)
print(p2.idade)