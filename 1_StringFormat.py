name = "naman"
nam1 = "rawat"
s = f"my name is {name} {nam1} amd i had joined techM"
print(s)


s1 = "my name is {}{}"
out = s1.format(name, nam1)
print(out)

print(name.title())
print(name.isalpha()) # will give true cuz of no space
print(name.isalnum())
print(name.isdigit())
ayush = "000numun00"
print(ayush.strip("0"))
print(nam1[::-1])
print(name.swapcase())


'''
.index()
.find()
.slicing using [start:end:step]



'''

string = "eivneoficndocious"
print(string[string.index("docious"):])

