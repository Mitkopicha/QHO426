#Initialise empty dictionary
d = {}
diction = dict()
#Initialise non-empty dictionary
phonebook = {"Thomas":79923797, "Aga":78889723973, "MD":9729878974}
#Print full dictionary
print(phonebook)
#Print/access individual elements
name = input("Who you gonna call: ")
if name in phonebook:
    print(f"Calling...{phonebook[name]}")
else:
    print(f"No number for {name}")
#Zipping two lists together to compose a dictionary
names = ["Garry","Ian","Laura"]
age = [56,21,16]
people = dict(zip(names,age))
print(people)
#Traversing dictionaries - accessing keys/values
for thing in people: #Method to print names
    print(thing)
for thing in people.keys():#Different method to print names
    print(thing)
for thing in people.values():#Method to print values and names
    print(thing)

for k, v in people.items():
    print(f"Person {k} is {v} years old")
