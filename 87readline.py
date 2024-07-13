try:
   file=open("F:\\PYTHON\\ajay.txt","r")
   print(file.readlines())
except Exception as e:
    print(e)