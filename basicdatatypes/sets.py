set1 = set()
print(set1)
set1.add(12)
set1.add(12)
set1.add(12)
set1.add(12)
set1.add(12)
set1.add(12)
set1.add(2)
set1.add(123)
set1.add(21)
set1.add(1234)
print(set1)
print()

mys_set = {1,2,3,4}
'''
mys_set.remove(4)#removes elements but raises error if not found
print(mys_set)
mys_set.discard(4)#does nothing if element not found
print(mys_set)
poped = mys_set.pop()#removes and returns an arbitary element
print(poped)
print(mys_set)

print(mys_set)
print(22 in mys_set)
print(4 in mys_set)
mys_set.clear()
print(mys_set)
'''

print()
set2 ={2,1,22,3,12}
print(set1-set2) #set difference A - B = ( A - (A & B) )
print()
print(set2-set1) #B - A = ( B - (A & B) )
print()
union_set = set1 | set2 #union , A | B = (A + B - ( A & B))
print(union_set)
print()
intersection_set = set1 & set2 #intersection, A & B = (A + B - (A|B))
print(intersection_set)
print()


