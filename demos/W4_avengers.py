def adding(lista = []): #Parametar will be a list
    new_member = input("Enter new hero: ")
    lista.append(new_member)


def removing(lista = []):
    rejected = input("Enter hero to be removed: ")
    if rejected in lista: #Using if statement because we are not sure if the item is in the list
        lista.remove(rejected)

def printing(lista = []):
    for hero in lista:
        print(f"The mighty {hero} is part of Avengers")

def run():
    avengers = []
    while True:
        opt = int(input("Avengers assemble!\n\n1-Add a member\n2-Remove a member\n3-Check on team\n9-Exit\nOption: "))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            removing(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 9:
            break
        else:
            print("Sort yourself out please!!!!")

run()