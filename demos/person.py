#The class #Person which is a blueprint for my objects to store info about humans
class Person:

    #Class Attribute -> attribute/feature acessible/applied to
    #every object of the class
    max_w = 200

    #Initialiser/Constructor -> function that is AUTOMATICALLY
    #called when an object is instantiated (magic method)
    #Initialiser of ANY class has the same name
    #"DUNDER" - Double underscore
    def __init__(self, name, age=0, job ="",w=100):
        #what are the instance attributes (features)
        #specific attributes to objects
        self.name = name
        self.age = age
        self.job = job
        if w > Person.max_w:
            self.weight = Person.max_w
        else:
            self.weight = w #class atribute


p1 = Person("Pesho", 29, "Machine",98)
p2 = Person("Mariq", 45, "Engineer",56)
p3 = Person("Udo",job="Headmaster")
p4 = Person("Gogo",w=600)

print(f"Person 1 is called {p1.name} and person 2 is called {p2.name}")
print(f"Together their total weight is {p1.weight+p2.weight}")
print(p1,p2,p3,p4)
print(f"{p4.name} weights {p4.weight}")
print(f"{p3.name} weights {p3.weight} and works as {p3.job}")

