import os


def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following: ")
    for file in os.listdir(path):
        print (file)
    return path


def run():
    print("Processing...")
    cwd()

run()