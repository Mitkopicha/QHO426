# Ask use for number of bars
n = int(input("How many bars should be charged? "))
# Declare a control variable
i = 0
while i<n:
    # Display bars
    print("Charging:", "█"*i)
    i=i+1
print("The battery is fully charged")