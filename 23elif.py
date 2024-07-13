days=int(input("Enter the days:"))
if(days==0):
    print("No fine")
elif(days<=5):
    print("Fine amount:",days*2)
elif(days>=6 and days<=10):
    print("Fine amount:",days*3)
elif(days>=11 and days<=30):
    print("Fine amount:",days*5)
else:
    print("Membership cancelled")