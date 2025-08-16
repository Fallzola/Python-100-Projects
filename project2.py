#Welcome to the tip calculator!
#What was the total bill? $
#How  much tip would you like to give? 10, 12, or 15?
#How many people to split the bill?
#Each person should pay: $40.00

print("Bem vindo a calculadora de gorjeta!")
bill = input("Qual foi a sua conta total? $")
tip = input("Quanto você gostaria de dar como gorjeta (porcentagem)? %")
people = input("Quantas pessoas vão dividir a conta? ")

total = (float(bill) + (float(bill) * (float(tip) / 100)) / float(people))

print(f"Cada pessoa deve pagar um total de: {total:.2f}$")