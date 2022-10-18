from tkinter import E
import random


a = 1
b = 35656222554887711
c = -3255522

print(type(a))
print(type(b))
print(type(c))

d = 1.10
e = 1.0
f = -35.59
g = 35e3
h = 12E4
i = -87.7e100

print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

j = 3 + 5j
k = 5j
l = -5j

print(type(j))
print(type(k))
print(type(l))

#converter de int para float:
x = float(1)
#converter de float para int:
y = int(2.8)
#converter de float para complex:
z = complex(x)

print(type(x))
print(type(y))
print(type(z))

num = random.randrange(1, 100)
print(num)