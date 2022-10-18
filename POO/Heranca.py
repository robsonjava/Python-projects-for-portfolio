class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    
    def nomeCompleto(self):
        print(self.nome, self.sobrenome)
    

p1 = Pessoa("Robson ", "Bento")
p1.nomeCompleto()

class Estudante(Pessoa):
    pass

p2 = Estudante("Alexandra ", "Silva")
p2.nomeCompleto()