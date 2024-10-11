

import random
import string
print("Welcome to Password Generator:")

noofletters = int(input("How many letters would you like in your password?\n"))
noofsymbols = int(input("How many symbols would you like?\n"))
noofnumbers = int(input("How many numbers would you like?\n"))

letters = string.ascii_letters
numbers = string.digits
symbols = ["@","$","&","!"]

'''
easy one 
--------
for i in range(noofletters):
    final_password += random.choice(letters)
for i in range(noofnumbers):
    final_password += str(random.choice(numbers))
for i in range(noofsymbols):
    final_password += (random.choice(symbols))

print("Password is",final_password) 

'''
final_pass = []
for i in range(noofletters):
    final_pass.append(random.choice(letters))
for i in range(noofnumbers):
    final_pass.append(str(random.choice(numbers)))
for i in range(noofsymbols):
    final_pass.append(random.choice(symbols))
random.shuffle(final_pass)
#final_password  = "".join(final_pass)
final_password = ''
for char in final_pass:
    final_password += char
print(final_password)

    
