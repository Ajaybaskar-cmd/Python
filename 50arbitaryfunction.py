#Arbitary function
def class_10(*student):
    print(student)
    print(",".join(student))
    for s in student:
        print(s)
    
class_10("ajay","rajesh","ragul")