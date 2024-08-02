a1 = ['python','java','c','c++']
b2 = [x for x in range(1,5)]
for i,j in zip(b2,a1):
    print(f"{i}. {j}")