string = """
Cut a slit into the chicken breast. Stuff it with mustard,
mozzarella and cheddar. Secure the whole thing with rashers of bacon. 
Roast for 20 minutes at 200C.
"""

counter = 1
ordered_list = str(counter) + '. '
for letter in string:
    if letter == '.':
      counter += 1
      ordered_list += '.\n'
      ordered_list += str(counter)
      ordered_list += '.'
    else:
      ordered_list += letter
no = len(str(counter))
print(ordered_list[0:-1-no])