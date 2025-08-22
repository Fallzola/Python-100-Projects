import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetCaps = []
for items in alphabet:
    alphabetCaps.append(items.upper())
numbers = ['1', '2', '3', '4', '5', '6', '7', '8' , '9', '0']
symbols = ['!', '@', '#', '$', '%', '&', '*', ')', '(']
i = 0
stringPassword = ''
confirmNumbers = int(input("Do you want numbers in your password?\n[1]Yes\n[2]No\n"))

usableLists = [alphabet, alphabetCaps]
password = []

match(confirmNumbers):
    case 1:
        usableLists.append(numbers)

confirmSymbols = int(input("Do you want symbols in your password?\n[1]Yes\n[2]No\n"))

match(confirmSymbols):
    case 1:
        usableLists.append(symbols)

lenght = int(input("How long do you want your password to be?\n"))

while i != lenght:
    listForKey = random.choice(usableLists)
    password.append(random.choice(listForKey))
    stringPassword = ''.join(password)
    print(stringPassword)
    i += 1
print(f"Your final password is: {stringPassword}\nAnd she has {len(password)} characters!")
