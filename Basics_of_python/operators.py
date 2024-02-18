#Arithmetic Operators
a=10
b=20
#concatenation
print(a+b)
print("Addition of a+b",a+b," Correct ")
print("Sub of a and b",a-b)
print("Mul of a and b",a*b)
print("Div of a and b",a/b) #returns a regular division 10/20 = 0.5
print("Quo of a and b",a//b)# it return a quotient
print("Rem of a and b",a%b)# it is a modulus , so it returns a reminder of the division
add=str(a+b)
print(type(add))
print(a**2) #square of num

#concatenation other approach
print("Addition of a+b",a+b)
name,age,gender="Mashood",26,"Male"
print("Name : %s , Age : %d , Gender : %s" %(name,age,gender))
#approach 2
print("Name : {} , Age : {}, Gender : {}" .format(name,age,gender))

#Relational Operators / Comparison Operators
# >,<,>=,<=,!=   - always returns a boolean values
#Logical Operators
# and or not - always returns a boolean values

