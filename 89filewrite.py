try:
    file=open("F:\\PYTHON\\test.txt","w")
    file.write("Ajay is a greatest business man and data analyst")
    file.close()
except Exception as e:
    print("File cannot open")
    
fp=open("F:\\PYTHON\\test.txt","r")
print(fp.read())