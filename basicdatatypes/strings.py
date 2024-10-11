'''
string is sequence of characters which are enclosed with single quotes or double quotes.'''
name = " Quality Thoughts ihub Python programming  "
#string index starts from 0 to n-1(n is length of string)
#index 0 or starting value of string


a = 'quality'
print(a)
first_index = a[0]
print("first index of 'quality': ",first_index) 
#prints "q" which is at 0
print()
last_index_1 = a[len(a)-1]
last_index_2 = a[-1]
#supports negative indexing from -1 from last to first
print('last index of "quality" : ',last_index_1)
print()
print('negative last index of "quality" : ',last_index_2)
print()
middle_index = a[3]
print('random in between index of "quality" : ',middle_index)
print()

print(name)
#length of string
length = len(name)
print('length of string of ',name,' is ',length)
print()
#captailzing string
captailzed = name.capitalize()
print('captailized string of name : ',captailzed)
#title
title = name.title()
print("title_text : ",title)
upper_case = name.upper()
lower_case = name.lower()
case_folded = name.casefold()
swapping_case = name.swapcase()
print('upper case text : ',upper_case)
print('lower case text : ',lower_case)
print('case folded text : ',case_folded)
print('swap case text : ',swapping_case)
print()


print('is alphanumeric : ',name.isalnum())
print('is digit : ',name.isdigit())
print('is lower : ',name.islower())
print('is upper : ',name.isupper())
print('is title : ',name.istitle())
print('is starts with " " :',name.startswith(" "))
print('is ends with " " :',name.endswith(" "))
print()


words = ['hello','world','is','wonderful']
joined_words = " ".join(words)
text = name.strip()
replaced_text = text.replace("Python Programming",'SQL')
print('orginal text = ',text)
print('replaced text = ',replaced_text)
print('words list joined together as ',joined_words)
print()


l_strip = name.lstrip()
r_strip = name.rstrip()
stripp = name.strip()
print('after removing whitespaces with using strip')
print('left strip = ',l_strip)
print('right strip = ',r_strip)
print('using strip = ',stripp)
print()


split_list = name.split()
print('list of words = ',split_list)
print('again we can use join() to get back the sentence')
joined_text = " ".join(split_list)
print('rejoined text is ',joined_text)


#string concatenation
name = 'Mandy'
greet = 'Hello'
world = 'World'
sentence = greet + '  ' + name + '  ' + ' welcome to python '+ world
print(sentence)