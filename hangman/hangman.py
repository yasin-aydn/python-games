import random

picture = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]


animals = ["elephant", "giraffe", "tiger", "monkey", "kangaroo",
                "dolphin", "penguin", "zebra", "rhino", "octopus",
                "cheetah", "gorilla", "hippo", "parrot", "koala"]

words = [chr(i) for i in range(97, 123)]

num_list = ["0","1","2","3","4","5","6","7","8","9"]
number_of_wrong = 0
letter = random.choice(animals)
true_list = list(q for q in letter)
words_with_blanks = list("_" for _ in range(len(letter)))
word_list = list()
print(words_with_blanks)

while True:
    debug = 0
    word = input("Insert a letter: ")
    word = word.lower()
    if not word in words:
        print("Insert a letter")
        continue
    if len(word) > 1:
        print("Insert only one letter")
    for q in word:
        if q in num_list:
            debug = 1
            continue
    if debug == 1:
        print("Insert a letter.")
        continue
    if word in word_list:
        print("This character is already inserted!")
        continue
    else:
        word_list.append(word)

    if word in letter:
        for q in range(len(letter)):
            if true_list[q] == word:
                words_with_blanks[q] = word
        print(picture[number_of_wrong])
        print(words_with_blanks)
    else:
        number_of_wrong += 1
        if number_of_wrong == 6:
            print(picture[number_of_wrong])
            print("YOU LOST")
            print(f"Correct Word:{true_list}")
            break
        print(picture[number_of_wrong])
        print(words_with_blanks)
    if not "_" in words_with_blanks:
        print("Congrats!")
        break

