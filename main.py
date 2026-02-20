print()
print("o——————————o")
print("| Quiz-LIT |")
print("o——————————o")
print()

print("Press [ENTER] to continue...")
input()

f = open("flashcards.txt")
terms = f.readlines()
f.close()

terms = [
    term.strip().split(",")
    for term in terms
]

print(terms)