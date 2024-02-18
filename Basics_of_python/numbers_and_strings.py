print(max(10, 54, 42, 2, 4, 66, 55))
l1 = [10, 3, 4, 33, 44, 1222]
print(max(l1))
print(min(l1))

str = "Mashood "
print(str + " khan")
print(str * 10)
# slicing in strings
print(str[0:3])  # slicing
print(str[0:-2])  # removes last 2 chars, counts spaces aswell

# get the ascii value of strings
ch='L'
print("Ascii value of : {} ".format(ch) ,"is : ",ord(ch))
str2="abcd"
print(max(str2)) # returns as per ascii values
print(min(str2))
print(len(str2))

for i in str2:
    print("test ",i)

str3 ="masd"
print("Mash" in str3)  #checks whether it is in string
print("----------------")
print(str3.isalnum()) #checks if string contains  number , returns true if there are only number in string
print(str3.isalpha()) #check alphabets
print(str3.isdigit()) #check digits
print(str3.capitalize()) #it capitalize the string
print(str3.isspace())
print(str3.isidentifier())
#There are many other string functions_and_scope_of_vars like :
# startswith,endswith,find,count,replace,swapcase(camelcase),upper,lower etc

#reverse the string
mystr="Farhan"
revstr=""
for i in mystr:
    revstr=i+revstr
print(revstr)
