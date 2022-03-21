#python program to find odd numbers in a range
Lower = int(input('enter the lower range:'))
Upper = int(input('enter the upper range:'))
for i in range(Lower,Upper):
    if (i%2==1):
        print(i)
