p = 5
sum = 0
count = 0
while p>0:
    count += 1
    f = int(input('enter a number : '))
    sum += f
    p -= 1
average = sum / count
print('average of 5 given numbers is ',average)