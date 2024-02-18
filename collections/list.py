
'''
There are four types of collections in python
1.List 2.Tuple 3. Set 4.Dictionary
'''

'''
1. List
List is a collection which is ordered and changable, Lists are mutable(can modify its elements)
and it is written in [].
'''
list1=[5,10,30,40,55,89]
print(list1) #prints all elements
print(list1[0]) #first element
print(list1[-1]) #last element

#get list values within the specified range
print(list1[1:4]) #prints [10,30,40]

#change list values
list1[0]=500
print(list1)

#iterate lists
for i in list1:
    print(i)
#add new item in the list
list1.append("Mashood")  #adds item at the end of rhe list
print(list1)

list1.insert(5,"khan") # Insert values based on index defined
print(list1)

#deleting items from list
list2=["Mashood","Farhan","khan"]
# list2.pop(0) #removes list by index , pop() will remove the last element(if not specified index)and returns
#removed element
removed_ele=list2.pop()
print(removed_ele," Removed")
print("Remaining ",list2)

list3=[1,2,3,4,5]
del list3[0]  #del wil delete the objects and doesnot returns any this
print(list3)

#clear function will remove all elements from the list
list3.clear()
print(list3)

#copy list items to other list
l1=[1000,3000,5000]
l2=list(l1)
print(l1)
print(l2)
#other approach for copy
l3=l2.copy()
print(l3)

#join/combine list
lj1=[10,20,30,40,50]
lj2=[60,70,80,90,100]
print(lj1+lj2)
lj3=["Mashood","khan","MCA","SE"]
lj4=[]
for i in lj3:
    lj4.append(i)
print(lj4)
#with extend function
lj5=[22,33,44,55]
lj6=[66,77]
lj5.extend(lj6)
print(lj5)


