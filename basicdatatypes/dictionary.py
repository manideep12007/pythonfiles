dict1 = dict()
print('empty dict is ',dict1)
dict2 = {'name':'manideep reddy',
         'city':'Hyderabad',
         'color':'red',
         'fav_number':25,
         'phone':9182642555}
'''
print(dict2)
print()
for keys,values in dict2.items():
    print(f'{keys} : {values}')
print(dict2.keys())
print(dict2.values())
print(len(dict2))
print()

dict3 = {'college':'gitam'}
dict4 = dict2.copy()
dict4.update(dict3)
print(dict4)

dict5 = {**dict2,**dict3}
print(dict5)

print(dict2.get('name'))
print()
print(dict2.items())
print()
print(dict2.pop('phone'))
print()
print(dict2.items())
print()
print(dict2.popitem())
print()
print(dict2.items())
'''
dict6 = dict2.copy()
print(dict6)
dict2.clear()
print(dict2)
