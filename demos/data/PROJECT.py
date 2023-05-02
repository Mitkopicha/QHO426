import csv

def reading():
    with open("hotel_reviews.csv") as rev:
        csv_reader = csv.reader(rev)
        ## next(csv_reader) # Progresses the lines in CSV (REMOVES HEADINGS)
        for row in csv_reader:
            print(row[2])


def writing():
    with open("hotel_reviews.csv", "a") as s:
        csv_writer = csv.writer(s)
        while True:
            name = input("Enter name: ")
            id = input("Enter ID: ")
            e1 = int(input("Enter Exam 1: "))
            e2 = int(input("Enter Exam 2: "))
            csv_writer.writerow([name, id, e1, e2]) #each looping it writes a new row to the csv file
            if input("Shall we stop? yes/no").lower() == "yes":
                break


writing()