try:
    fp=open("F:\\PYTHON\\aaa.txt","r")
    for line in fp:
        print(line)
        
except Exception as e:
    print(e)
    
fp=open("F:\\PYTHON\\aaa.txt","r")
print(fp.readlines())
