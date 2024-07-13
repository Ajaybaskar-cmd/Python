try:
    a=10/2
    print(a)
    b=[100,20,30]
    print(b[1])
except ZeroDivisionError:
    print("Cant divisible by zero")
except IndexError:
    print("Invalid index")