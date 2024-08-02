year = int(input('year : '))
if year%4 == 0:
    if year%100 ==0:
        if year%400==0:
            leap=True
        else:
            leap =False
    else:
        leap = True
else:
    leap = False
if leap:
    print(f'{year} is leap year!!')
else:
    print(f'{year} is not leap year!')