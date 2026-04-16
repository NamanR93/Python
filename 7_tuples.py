# tuples r immutable means we cannot do anything

nums = (1,2,3)
print(nums.index(2))
print(nums.count(2))

# to add item to tuple covert it into list add then back to tuple

list = ("mango",) #tuple with single data

n = int(input("enter the index:"))
tuple = (1,2,3,4,5)
print(tuple.index(n))
