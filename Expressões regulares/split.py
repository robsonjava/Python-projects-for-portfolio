import re

txt = "O calor do motor da moto"

x = re.split("\s", txt, 3)

print(x)