import platform

x = platform.system()
print(x)

# Listar todos os menbros

x = dir(platform)
#print(x)

for item in x:
    print(item)