age = int(input("Enter age: "))
ch = int(input("Enter number of children"))

if age > 25 and ch > 0 and age<55: #AND->ALL NEED TO BE TRUE
    print("You are a parent!")
    print(f"Next year you wii be {age+1}years old")
elif age > 55 and ch > 0:
    print("Hopefully you will get support when you are older")
elif age < 18 or ch ==0: # OR-> AT LEAST 1 to be TRUE
    print("Plenty of time to have kids. \nNo rush!")
else:
    print("You are not so young")