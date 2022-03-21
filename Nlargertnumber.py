#Python program to find N largest number in a list
n = int(input('enter the length of list'))
l = []
for i in range(n):
    e = int(input('enter the element'))
    l.append(e)
    print(l)
l.sort()
print('Nth largest number is:',l[n-1])

