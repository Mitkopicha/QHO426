# Ask user for markings
print("What strange markings do you see? ")
m = input()
i = 1
# Use for loop to identify each marking and display them appropriately
for position in range(0, len(m), 1):
    print(f"index {i}: ",end="")
    i = i + 1
    print(m[position])

print("Done!")