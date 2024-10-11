numbers = [
    x for x in range(1,100)
]
print('Multiplies of 5 are : ')
for n in numbers:
    if n%5 == 0:
        print(n,end=',')