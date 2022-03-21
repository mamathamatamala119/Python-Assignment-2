#Different ways to Clear a list in python
l = ['a','d','g','h']
#Using clear method
l.clear()
print(l)
#Using remove method
l2 = [1,2,3,4]
l2.remove(1)
l2.remove(2)
l2.remove(3)
l2.remove(4)
print(l2)
#Using delete method
l3 = ['mamatha','renu','deva']
del l3[:]
print(l3)
#Using pop method
l4 = ['mamatha','march']
l4.pop()
print(l4)
#using null set
l5 = [1,2,4,5]
l5 = []
print(l5)