import json

x = '{"nome":"Robson", "idade":36, "cidade":"São Paulo"}'

y = json.loads(x)
print(y)
print(type(y))

print(y["nome"])
print(y["idade"])
print(y["cidade"])