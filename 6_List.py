# List -> we can modify the list

name = ["john", "naman"," madhav","rosi"]
print(name[:])  # this will new list

num =[3,6,2,8,4,10]

largest = num[0]
for x in num:
    if x> largest:
        largest = x
print(largest)

# 2D list
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in matrix:
    for j in i:
        print(j)


# List Methods

nums = [1,2,3,4]

print(nums.append(5)) # will append the no at the end

nums.insert(1,1.5)    # add the no at ith index
print(nums)

nums.remove(5)        # remove the no
print(nums)

#nums.clear()         # empty the list

nums.pop()            # remove the item from end 
print(nums)

nums.index(3)         # will give the index of no

print(50 in nums)     # return true or false

print(nums.count(1))  # return count

nums.sort()           # sort the list
print(nums)

nums2 = nums.copy()