temp = float(input("Enter your body temperature: "))

if temp > 38:
    print("You have a fever!")
elif temp<36:
    print("You have low temperature.")
elif temp == 37:
    print("You have a standard body temperature!")
else:
    print("You either typed in wrong value or you no fever!")

print("Your temperature is {}C".format(temp))
#Indentation specifies the coe block - collection of related statements in Python