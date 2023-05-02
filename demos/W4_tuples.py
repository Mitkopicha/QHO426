#Declare a tuple
x = ("Piotr", 68, True)
y = tuple(["Garry", 32, False])

#Print tuples
print(x)
print(y)
print(x[1])
#Cannot change idividual items
#        x[1] = 69

#Concatenate tuples
z = x + y
print(z)
print(y)
print(x)

#Using min and max functions
h = (74, 68, 45, 35, 15, 1, 82)
print(min(h))
print(max(h))

#Swapping items in tuple a little cheat
lista = list(h)
temp = h[0]
lista[0] = lista[1]
lista[1] = temp
h1 = tuple(lista)
print(h1)
