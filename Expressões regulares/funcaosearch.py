import re

txt = "O calor do motor da moto"

x = re.search("\s", txt)

print(x)

x = re.search("Brasil", txt)
print(x)