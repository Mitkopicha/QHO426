while True:
    print("Chose on of the following: \n1-Nice message\n2-Aream pf rectangle:\n3-Area of triangle\n4-Times table\n5-Exit")
    opt=int(input)
    if opt == 1:
        print("You do not smell so bad today")
    elif opt == 2:
        h = float(input("Enter height: "))
        b = float(input("Enter the base:  "))
        area = h * b
        print(area)
    elif opt == 3:
        print("Base of triangle ")
        base = float(input())
        print("Height of triangle")
        height = float(input())
        print((base * height) / 2)
    elif opt==4:
        n = int("Enter whole number: ")
        for i in range(1, 11):
            print(f"{n}x{i}={n*1}")
    elif opt == 5:
        break
    else:
        print("No such option!!")
