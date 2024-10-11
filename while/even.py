n = int(input('enter till which number : '))
sum = 0
i = 0
while i <= n:
    if i%2 == 0:
        print(i,end=' ')
        sum += i
    i += 1
print(f'\nsum of {n} even numbers is {sum}')