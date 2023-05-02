#Declare empty list
bleh = []
meh = list()
#Declare a non-empty list
yummy = ["Chicken","Ice cream","Chocolate"]
#Print entire list

print(yummy[-3])
#Print some items
print(yummy[1:3])

#Add elements to our list (expand it) - adding at the top of the the list
print(bleh)
bleh.append("Marmite")
bleh.append("blehhh")
print(bleh)
yummy.append("PIEROGGI")
print(yummy)

#Add multiple items to a list
n = int(input("How many items to add:"))
for i in range(n):
    bleh.append(input("Enter horrible food: "))
print(bleh)
bleh.extend(["Horse meat", "Pancakes"])
print(bleh)

#Inser items at specific positions on the list
bleh.insert(1, "Cabbage")
print(bleh)
bleh.insert(4, "Onions")
print(bleh)

#Remove item from the list
if "Carrot" in bleh:
    bleh.remove("Carrot")
if "Tato" in bleh:
    bleh.remove("Tato")
print(bleh)

#Remove items by index
x = bleh.pop(5) #Returns that value
print(x)
print(bleh)

#Alternative way of deleting by index
del bleh[4]
print(bleh)

#CHeck a list for particular data type
listaaa = ["Fred", 56, True, 99.4, "Potato", True, 82]
#True has a numerical value of 1 and False has 0
for item in listaaa:
    if isinstance(item,str):
        #print(item, end="**@**")
        sum += item
print(sum)


