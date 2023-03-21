# Ask user for number
print("Please enter a number: ")
number = int(input())
# Calculating factorial
count = 0
total = 1

while count < number:
    count = count+1
    total = total*count
print("The factorial is",total)
