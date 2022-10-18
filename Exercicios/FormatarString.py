a = "Robson Bento"
b = "Santos"
c = a + " " + b
print(c)

idade = 35
txt = "Eu sou Robson e tenho {} anos de idade"
print(txt.format(idade))

quantidade = 3
item = "bolo"
valor = 14.99
meuPedido = "Eu quero {} pedaços de {} por {} reais."
meuPedido2 = "Eu quero {} pedaços de {} por {} reais."
print(meuPedido.format(quantidade, item, valor))
print(meuPedido2.format(quantidade, item, valor))