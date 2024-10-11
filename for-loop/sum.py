n = int(input('last number : '))
list1 = [l for l in range(1,n+1)]
sum = 0
for n in list1:
    sum += n
print(f"sum of n numbers from 1 to {n} is {sum}")
#sum of n natural numbers