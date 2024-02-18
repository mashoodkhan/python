'''
2.Tuple is an collection which is ordered and immutable which means unchangable
  it is defined in round brackets ()

  Mutable means we cannot to following things:
  1. Cannot append a new value
  2. Cannot modify/change any value
  3. Cannot remove any value
  4.Cannot insert any value
 '''
t1=(10,30,40)
print(t1)
'''
#range , printing ,reading all values, printing within the range is similar to list
Difference between list and tuple , we cannot change the tuple values
If we want to change the tuple value , we need to convert tuple into list
Cannot add or remove values from the tuple
'''
t2=("Mashood","kan")
print(t2)
l1=list(t2)
l1[1]="Khan"
print(l1)
#convert back to tuple
t2=tuple(l1)
print(t2)

#copy is possible
t3=tuple(t2)
print("t3 ",t3)

#join is possible


