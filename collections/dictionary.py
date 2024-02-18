'''
Dictionary stores the values in key value pairs,These are mutable,unordered and have indexes
'''
dict1={
    "name":"Mashood",
    "id":101,
    "city":"hyd"
}
# print(dict1["name"])
# print(dict1.get("name"))

for i in dict1:
    print(i) # this prints only keys
for i in dict1.values():
    print(i)#prints values
for i,j in dict1.items():
    print(i,":",j)

#Add new item
dict1["pin"]="500008"
print(dict1)
#remove item
dict1.pop("pin")
print(dict1)
#copy
dict2=dict1
print(dict2)
dict3=dict2.copy()
print("dict 3",dict3)
#remove
del dict1["name"]
del dict1
#print(dict1)


list=[]
for i in list:
    i.append(1)
    i.append(2)
    i.insert(3,1)
print(list)