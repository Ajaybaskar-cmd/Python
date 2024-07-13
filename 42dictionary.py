#dictionary

user={"name":"Ajay","age":25,"gender":"male"}
print(user)
print(type(user))

#get the value
print(user["name"])
print(user.get("age"))

#keys
print(user.keys())

#values
print(user.values())

#items
print(user.items())

#dictionary using of for loop
for x in user:
    print(x,':',user[x])
    
#values of for lloop
for x in user.values():
    print(x)
    
#keys of for loop
for x in user.keys():
    print(x)
    
#for loop of items 
print("Item\n")
for x,y in user.items():
    print(x,":",y)
    
#if condition check in dictionary
if "age" in user:
    print("yes")
    
#adding the new value and key
print(user)
user.update({"martial":"single"})
print(user)

#changing the value for key
user["age"]=35
print(user)

#remove the key and value using pop
user.pop("martial")
print(user)

#clear the values and key
user.clear()
print(user)

#delete the variable
del user

#nested dictionary
users={
    "user1":{
        "name":"ajay",
        "age":21,
        "gender":"male"
    },
    "user2":{
        "name":"ragul",
        "age":21
    }
}

print(users)

