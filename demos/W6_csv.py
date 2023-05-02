import csv

def reading():
    with open("students.csv") as students:
        csv_reader = csv.reader(students)
        next(csv_reader) # Progresses the lines in CSV (removes headers)
        for row in csv_reader:
            print(f"{row[0]} received marks of {row[2]}, {row[3]}")

def writing():
    with open("students.csv", "a") as s:
        csv_writer = csv.writer(s)
        while True:
            name = input("Enter name: ")
            id = input("Enter ID: ")
            e1 = int(input("Enter Exam 1: "))
            e2 = int(input("Enter Exam 2: "))
            csv_writer.writerow([name, id, e1, e2])
            if input("Shall we stop? Y/N").upper() == "Y":
                break


writing()