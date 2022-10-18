import re

txt = "O calor do motor da moto"

x = re.findall("or", txt)
if x:
    print("Existe!")
else:
    print("Não existe!")