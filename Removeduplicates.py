#python program to remove duplicate from a list 
l = [4,5,4,6,5,7,6]
print(l)
l1=set(l)
print('l1:',list(l1))
for i in l:
    if i not in l1:
        l1.append(i)
        print(i)