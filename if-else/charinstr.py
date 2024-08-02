'''
Exercise 3: Check If a Character Is in a String
Exercise: Write a program to ask the user to do the following:

Provide the name of a country that does not contain any lowercase a or e letters.
 (Use the prompt: The country is: )
If the user provides a correct string (i.e. one with no a or e inside it),
 print: You won... unless you made this name up!
Otherwise, print: You lost!
'''
country = input('enter a country name : ')
if 'a' not in country and 'e' not in country:
    print('You won.., unless you made this name up!')
else:
    print('You lost!')