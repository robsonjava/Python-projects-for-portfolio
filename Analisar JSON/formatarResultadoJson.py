import json

x = {"nome":"Robson", "idade":36, "cidade":"São Paulo"}

#print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))