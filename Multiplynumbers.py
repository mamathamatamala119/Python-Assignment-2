#python program for multiply all the numbers in list
l = [2,5,4,7]
print(l)
temp = 1
for i in range(0,len(l)):
    temp = temp*l[i]
    print('multiply all the elements:',temp)
