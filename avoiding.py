n = int(input("How many live cables mush i avoid? "))
t = int(0)
while t < n:
    print("Avoiding..", end="")
    print(f"Done! {n} live cable avoided")
    n=n-1
print("\nAll live cables have been avoided")