'''
Set : Set is a collection which is unordered and unindexed and it is immutable, Sets are written in curly braces{}
1.Set is an ordered list which stores data in random order , it doesn't have index
2.Set doesn't allow duplicate values , Means if there are any duplciate vlaues in any external source,
if we use set then it doesn't print it
'''

set1 = {"apple", "banana", "orange", "banana"}
print(set1)
for i in set1:
    print(i)

# Add new items to set
set1.add("Grapes")  # adds single items to a set
print(set1)

set1.update(["Strawberry", "mango"])  # adds multipe items in a set
print(set1)

# Removing items from the set
'''
remove():it removes the items from the set, if we try to remove value which is not present
it throws key error

discard(): also removes value , but it doesn't throw any error if value is not present
'''
set1.remove("banana")
print("Removed ", set1)

#clear everythings from set
set1.clear() #it clears all values from set
print(set1)

del set1  #deletes set variable aswell

#Joining two sets
s1={1,2,3,4,5}
s2={6,7,8,9,10}
s3=s1.union(s2)
print(s3)



