# Pode ser usada em qualquer parte do codigo

x = 300

#def myfunc():
#    print(x)

#def myfunc():
#    x = 200
#    print(x)

def myfunc():
    global x
    x = 299
    print(x)
    

myfunc()

print(x)