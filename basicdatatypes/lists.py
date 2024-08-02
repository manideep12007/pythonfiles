num_list = [1,2,3,4,5,6,7,8,9,10]
print(num_list)
num_list.append(9)
print('after appending 9 :',num_list)
num_list.remove(9)
print('after removing first 9 : ',num_list)
num2_list = [11,21,33]
num_list.extend(num2_list)
print('after extending with num2_list : ',num_list)
num_list.insert(5,100)
print('after inserting 100 at 5th index : ',num_list)
poped_list = []
for i in range(1,4):
    poped_list.append(num_list.pop(i))
print('after poping out 1 to 3 index values ',num_list)
print('poped out list was ',poped_list)
print('occurence of 9 in list ',num_list.count(9))
num_list.sort() #defalut reverse=False Ascending order
print('sorted list in AO : ',num_list)
num_list.sort(reverse=True) #descending order reverse=True
print('sorted list reverse=True : ',num_list)
num_list.reverse() #reverse the sort / list 
print('reverse the list : ',num_list)
