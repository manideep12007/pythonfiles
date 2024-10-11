z = 1
while z <= 15:
    if z%3 == 0 and z%5 == 0:
        print(z,'fizzbuzz')
        z+=1
    elif z%3 == 0:
        print(z,'fizz')
        z +=1
    elif z%5 == 0:
        print(z,'buzz')
        z+=1
    else:
        print(z)
        z += 1
    