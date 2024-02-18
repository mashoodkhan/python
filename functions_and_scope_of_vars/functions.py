'''
function : It is a set of statement which performs a well defined task
main purpose of function is re usability

'''

def my_func():
    print("Hello world")
my_func()

#parameterized functions_and_scope_of_vars
def add(a,b):
    return a+b

print(add(10,30))

#global variable : accessible in whole file
myglobal="Global Variable"
print(myglobal)

#local variable : accessible within the scopee of class or function
def  localfun():
    mylocal = "Local Variable"
    print(mylocal)
localfun()

#global
xy = 10000
def globalFunc():
    global xy
    xy=90000
    print(xy)
#this we can access outsite
print(globalFunc())

def  getListOfItems():
    list1 = [10, 20, 30, 40, 50]
    return list1
print(getListOfItems())
