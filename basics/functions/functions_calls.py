def box(word):
    length = len(word)
    print("#"*(length+4))
    print("# " + word + " #")
    print("#"*(length+4))




def low(word):
    print(word.lower())


def upper(word):
    print(word.upper())

 


def mirror(word):

    print(word, " | ", word[::-1])
  #SLICING - act of sepratating/accessing individual items
  #of a list OR character in a string
  #Slice using{start,end,step)
  #word = "This is sparta!"
  #print(word[::-1])


def repeat():
    word = input("Whats the word? ")
    r = int(input("How many times to display the word? "))
    for i in range(0, r, 1):
        if i % 2 == 0:
            print(word.lower())
        elif i % 2 == 1:
            print(word.upper())
        else:
            print(word.upper())




def spastic_writing(word):
    for i in range(len(word)):
        if i % 2 == 0:
            print(word[i].upper(), end = "")
        else:
            print(word[i].lower())




def run():
    w = input("Enter a word: ")
    print("Choose an option:\n1-Box\n2-Lowe Case\n3-Upper Case\n4-Mirror\n5-Spastic Writing")
    opt = int(input())
    if opt == 1:
        box(w)
    elif opt == 2:
        low(w)
    elif opt == 3:
        upper(w)
    elif opt == 4:
        mirror(w)
    elif opt == 5:
        repeat(2)
    elif opt == 6:
        spastic_writing(w)
    else:
        print("No such option, go to Specsavers!")

run()