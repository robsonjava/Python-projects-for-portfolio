x = ("Gabriel", "Danny", "Arthur")
print(x)

y = list(x)
y[1] = "Danielle"
x = tuple(y)
print(x)

# y = list(x)
# y.append("Lucas")
# x = tuple(y)

y = ("Lucas",)
x += y
print(x)

y = list(x)
y.remove("Arthur")
x = tuple(y)
print(x)

del x
print(x)