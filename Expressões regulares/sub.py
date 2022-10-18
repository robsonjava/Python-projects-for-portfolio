import re

txt = "O calor do motor da moto"

x = re.sub("\s", "9", txt)

print(x)

num1 = "11 913134818 11 947182569"

y = re.sub("11 9", "9", num1)
print(y)