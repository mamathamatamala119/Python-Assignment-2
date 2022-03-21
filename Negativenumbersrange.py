#python program to find all positive numbers in range
Lower = int(input('enter the lower range'))
Upper = int(input('enter the upper range'))
for i in range(Lower,Upper):
    if i<0:
        print(i)