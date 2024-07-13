#arbitary keyword function
def biodata(**data):
    print(data)
    for i in data:
        print(i,":",data[i])
    
biodata(name="Ajay",age=21,gender="male")
