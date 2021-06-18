pic = int(input("How many pictures you would use each month"))
text = int(input("How many texts you would use each month"))
data = int(input("How many data you would use each month"))

piccost = pic*0.35
textcost = text*0.10
datacost = data*0.05

totalcost = piccost+textcost+datacost

print(totalcost)

if totalcost >= 10:
    print("You would be better on a contract")
else:
    print("You don't have to get a contract")
