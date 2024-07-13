days=int(input("How many days :"))
if days==0:
    print("No fine")
elif days<=5:
    print("Pay the fine for 10 rupees")
elif days>=6 and days<=10:
    print("Pay the fine for 20 rupees ")
elif days>=11 and days<=30:
    print("Pay the fine for 100 rupees")
else:
    print("Membership cancelled")