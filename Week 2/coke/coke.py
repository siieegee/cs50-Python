# Initial Amount Due
amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    cents = int(input("Insert Coin: "))
    if cents in [25, 10, 5]:
        amount_due = amount_due - cents

change_owed = abs(amount_due)
print("Change Owed:", change_owed)
