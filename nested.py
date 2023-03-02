# Ask user for input identified as int
rows = int(input("How many row's would you like? "))
col = int(input("\nHow many columns would you like? "))
# Use nested for loop to display emojis
for row in range(0, rows, 1):
    for column in range(0, col, 1):
        print(";P", end="")
    print()
print("\nDone!")