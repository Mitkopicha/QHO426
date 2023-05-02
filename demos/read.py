import os

def search(one = 1):
    print("Searching...")
    with open("locationss.txt") as file:
        for line in file:
         # do something with the line from the file
            # line.strip() will remove any white space including the \n character
    print(f"Looked in {line}")
    print("...Done!")


def run():
    search(data/files/txt/locations.txt)