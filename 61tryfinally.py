try:
    a=10/0
except Exception as e:
    print(e)
else:
    print(a)
finally:
    print("Thank you")