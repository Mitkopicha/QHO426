n1 = float(input("Choose a number:"))
n2 = float(input("Please choose a second number:"))
print(f"{n1:.1f} + {n2:.1f} = {n1+n2}")  #f-string approach
print("{} - {} = {}".format(n1,n2,n1-n2))  #format method
print(str(n1) + " x " + str(n2) + " = " + str(n1*n2)) #string concatenation
print(str(n1), "/", str(n2), "=", str(n1/n2)) #Comma separated
print(f"{n1}^{n2}={n1**n2}")
print(f"{n1} % {n2} = {n1%n2}") # Modulo operator->calculating remainder of division