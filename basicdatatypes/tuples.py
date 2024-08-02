num_tuple = (1,2,3,4,5,6,7)
print(num_tuple)
print(num_tuple.index(5))
print(num_tuple.count(5))
print(len(num_tuple))
num_list = [1,2,3]
num_tup = tuple(num_list)
print(f'list {num_list} to tuple {num_tup}')
print()
print('max of num_tuple is ',max(num_tuple))
print('min of num_tuple is ',min(num_tuple))
print('sum of num_tuple is ',sum(num_tuple))
print('avg of num_tuple is ',sum(num_tuple)/len(num_tuple))


