'''
Exercise: Write a program that will ask the user for their height in centimeters.
 Use the input() built-in function to do this.
 If the height is more than 185 centimeters, print the following line of code:'''

height = float(input("What is your height (in Cms)?\n"))
if height>185:
    print(f"your are very tall")
else:
    print(f"you are very short")