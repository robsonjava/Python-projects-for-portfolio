import re


txt = "O Gabriel amigo do Miguel"

x = re.search("^O.*Miguel$", txt)

if x:
    print("SIM! Nós temos uma correspondência")
else:
    print("Nenhuma correspondência!")