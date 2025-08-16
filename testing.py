import sys

from project2 import total

print("Welcome to Python Pizza! 🍕")
size = input("What size do you want?\n[S]Small $15\n[M]Medium $20\n[L]Large $25")
extra = input("Do you want extra pepperoni?\n[Y] Yes, I want (+2$)\n[N]No, I don't want")

size.upper()
extra.upper()

if extra == "Y":
    extra = 2
else:
    extra = 0

if size == "S":
    size = 15
elif size == "M":
    size = 20
elif size == "L":
    size = 25
else:
    print(f"There is no such size as '{size}'\nTry again.")
    sys.exit()

total = size + extra

print(f"Seu pedido ficou em {total}!")