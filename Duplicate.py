#python program to find duplicate from a list of integers
l = [4,5,4,6,5,7,6]
print(l)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i)
print('after removing duplicate numbers:'l1)        
