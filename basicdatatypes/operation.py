my_list = [x for x in range(2,20,2)]
my_tuple = tuple(x for x in range(2,20,2))
print(my_list)
print(my_tuple)
my_list = [1, 2, 3]
for item in my_list:
    print(item)

my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)

#tuple unpacking
tup = (1,2,4,5)
a,b,c,d = tup
print(a,b,c,d)

nested_list = [[1, 2], [3, 4]]
nested_tuple = ((1, 2), (3, 4))
print(nested_list[1][0])  
print(nested_tuple[1][0]) 

print(sum(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
