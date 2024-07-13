#string and string function
s="ajay"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("a"))
print(s.endswith("a"))
print(s.find("a"))
print(s.find("a",2))
print(s.replace("a",'0'))
a="ajay1223"
print(a.islower())
print(a.isupper())
print(a.isalnum())
print(a.isalpha())
s="ajay\nis\ndata\nanalyst"
print(s.splitlines())
print(s.splitlines(True))
a="     ajay"
print(a.split(" "))
print(len(a))
print(len(a.strip()))
s="28-01-2002"
print(s.partition("-"))