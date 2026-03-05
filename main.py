# dep

import random


# const

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# title screen

print()
print("o——————————o")
print("| Quiz-LIT |")
print("o——————————o")
print()

print("Press [ENTER] to continue...")
input()


# read/parse flashcards file

f = open("flashcards.txt")
terms = f.readlines()
f.close()

for i, term in enumerate(terms):
    terms[i] = term.strip().split(",")


# choose random term

random.shuffle(terms)


# loop through all flashcards

for to_test in terms:
    # define possible definitions

    definitions = { to_test[1] }

    while len(definitions) < 4:
        definition_idx = random.randrange(
            0, len(terms)
        )
        definition = terms[definition_idx][1]
        definitions.add(definition)

    definitions = list(definitions)
    random.shuffle(definitions)


    # ask the user for the answer

    print("What is the definition to...")
    print(to_test[0])

    for i, definition in enumerate(definitions):
        letter = ALPHABET[i]
        print(f"{letter}) {definition}")


    # user guesses

    guess_idx = -1
    while True:
        guess_idx = input("> ").upper()
        if len(guess_idx) == 1 and guess_idx in ALPHABET:
            guess_idx = ALPHABET.index(guess_idx)
            if guess_idx < len(definitions): break

    guess = definitions[guess_idx]
    correct = guess == to_test[1]

    print("You got it!!!!" if correct else "Uh oh you're dumb...")
    print()