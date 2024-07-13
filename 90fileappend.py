try:
    file=open("F:\\PYTHON\\test.txt","a")
    file.write("\nAjay is promote to data scientist")
    file.close
    
    fp=open("F:\\PYTHON\\test.txt","r")
    print(fp.read())

except Exception as a:
    print(a)
    
    
f=open("f.txt","r")
print(f.read())