list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

#Formato tradicional
list3 = list1 + list2
print(list3)


#Formato com um for
for x in list2:
    list1.append(x)

print(list1)

#Metedo Extend

list1.extend(list2)
print(list1)
