money = float(input("How much money you spent? "))

if money >= 10:
    print("You will get $1 voucher to spend next time you come in the store")
elif money >= 20:
    print("You will get $3 voucher to spend next time you come in the store")
else:
    print("You will not get any voucher")
