people = int(input("How much people there are? "))
tip = float(input("How much percentage the tip should be? "))
bill = float(input("How much the bill comes in? "))

billSplit = bill / people
billTotal = bill * 1,tip

print("Each people must pay", billSplit, "The total bill with tip is", billTotal)
