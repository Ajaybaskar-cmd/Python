#Name error
try:
    print(a)
except NameError:
    print("A is not defined")
    
#ZeroDivisionError
try:
    a=10/0
except ZeroDivisionError:
    print("Denominator can't be zero")
    
#Value error
try:
    a=int("ajay")
except ValueError:
    print("Please enter numbers only")
    
#Index Error
try:
    a=[10,20]
    print(a[4])
except IndexError:
    print("Invalid index")