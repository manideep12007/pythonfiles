n = int(input('enter a number : '))
reverse_n = 0
while n != 0:
    digit = n % 10
    reverse_n = reverse_n * 10 + digit
    n = n//10
print('reverse number is ',reverse_n)