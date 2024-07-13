try:
    file=open("F:\\PYTHON\\aaa.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")