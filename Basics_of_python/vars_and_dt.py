import keyword
# #Strings
# name="Mashood khan"
# print(name)
# #Integers
# x = 10
# print(x)
# #floats
# y=10.6
# print(y)
# #Boolean
# bool=True
# print(type(bool))
# #Double
# z=10.555
# print(z)
######################

# str="Mashood"
# str2="khan"
# print(str+" "+str2)
#
# #keywords
# print(keyword.kwlist)
#
# myKeyword='async'
# print(keyword.iskeyword(myKeyword))
# if(keyword.iskeyword(myKeyword)):
#     print("Yes "+myKeyword+" is a keyword in Pyhton")
# else:
#     print("No "+myKeyword+" is not a keyword in Python")
#
# #datatypes and check the types of var
# a=10
# b="Mashood"
# print(type(b))

#creating multiple vars in single statement at once
c,d,e=10,20,'Mashood khan'
x=y=z=100
print(c,d,e)
print(x,y,z)

#swapping of two numbers
s1=10
s2=20
temp=s1 #temp =10
s1=s2 # s1=20
s2=temp
print(s1,s2)


a1=100
a2=200
c=a2 #c=200
a2=a1 #a2=100
a1=c
print(a1,a2)

#easy way of swapping in python
x1=5
x2=10
x1,x2=x2,x1
print(x1,x2)

#List
y1=[10,20,30,40]
#print(type(y1))
print("printing ,,,")
print(y1[2])
#set
z1={"Mashood","Khan","Farhan"}
#rint(type(z1))


#deleting a variable
d1=10
print(d1)
del d1
print("deleted d1")
print(d1)