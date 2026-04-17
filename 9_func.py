def greet_user():
    print("hi there")

greet_user()
print("finish")

# now the func with argu and parameter
# parameter is the value we define for receving info
# argu is the actual piece of info we supply at time of func calling

def name(fname, lname):
    print(f"my name is {fname} {lname}")


name("naman","rawat")


#with return statement

def square(num):
    return num*num

print(square(9))