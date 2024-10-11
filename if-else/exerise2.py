'''
write a program that will ask
user following
Is New Delhi the capital of India?
If the user answers n, print: Wrong! New Delhi is the capital!
If the user answers y, print: Correct!
If the user answers anything else, print: I do not understand your answer!'''
answer = input('Is New Delhi is the captail of India?\n')
if answer == 'y':
    print('Correct!')
elif answer == 'n':
    print('wrong! New Delhi is the captail!')
else:
    print('I do not understand your answer!')