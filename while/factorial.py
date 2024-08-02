n = int(input('number : '))
temp = n
factorial = 1
while temp != 0:
    factorial *= temp
    temp -= 1
print(f"factorial of {n} is {factorial}")