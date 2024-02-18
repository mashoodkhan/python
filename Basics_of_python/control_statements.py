# conditional statements
# if , if else , elif
a1 = 10

if (a1 >= 25):
    print("Passed!")
elif (a1 > 25 and a1 < 50):
    print("passed with good percentage")
else:
    print("Failed")

# looping statements
# for while
l1 = [10, 20, 30, 40]
for i in l1:
    print(i)

# print even and odd numbers bw 1 to  50 and for range bw 20 to 30 print odd rest all even
my_even_list = []
my_odd_list = []
my_range = range(51)
for i in my_range:
    if i % 2 == 0 and not (20<i<30) :
        my_even_list.append(i)
    if i%2!=0 and 20 < i < 30:
        my_odd_list.append(i)
print("Even Numbers list  ", my_even_list)
print("Odd Numbers list ", my_odd_list)

# while
# n=1
# while(n<10):
#     print(n)
#     n=n+1
# Jumping statements
# break #continue
for i in range(10):
    if i==5:
        break
    print(i)
for i in range(10):
    if i==5:
        continue
    print(i)