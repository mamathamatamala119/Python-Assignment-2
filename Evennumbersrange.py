#Python program to find all even numbers in a range
Lower = int(input('enter the lower range:'))
Upper = int(input('enter the upper range'))
for i in range(Lower,Upper):
    if (i%2==0):
        print(i)