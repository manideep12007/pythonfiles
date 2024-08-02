#descending order
numbers = [12,23,12,3,6,66,32]
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]<numbers[j]:
            temp = numbers[j]
            numbers[j]=numbers[i]
            numbers[i]=temp
print(numbers)