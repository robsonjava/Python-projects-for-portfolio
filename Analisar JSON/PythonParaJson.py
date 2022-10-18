import json

x = {
    "nome":"Robson",
    "idade":36,
    "cidade":"São Paulo"
}

y = json.dumps(x)

print(y)
print(type(x))
print(type(y))