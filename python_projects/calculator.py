
import os

def addition(num1,num2):
    return num1 + num2

def subraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        return 'You cannot be determine'

def power(num1,num2):
    return num1**num2

def main():
    
    start_game = True
    number1 = None
    
    while start_game:  
        
        if number1 is None:
            number1 = eval(input("Enter first number : "))  
                
        opertion = input("'+'\n'-'\n'*'\n'/'\n'**'\n :- ")
        while opertion not in ['/','*','+','-','**']:
            print("please select correct operation")
            opertion = input("+\n-\n*\n\/\n**")  
              
        number2 = eval(input("Enter next number : "))
        
        if opertion == '+':
            result = addition(number1,number2)
        elif opertion =='-':
            result = subraction(number1,number2)
        elif opertion =='*':
            result = multiplication(number1,number2)
        elif opertion =='/':
            result = division(number1,number2)
        else:
            result = power(number1,number2)
        
        print(f"{number1} {opertion} = {result}")
        
        
        choice = input(f"enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit :  ").lower()
        while choice not in ['y','n','x']:
            print("pick right input y/n/x")
            choice = input(f"enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit :  ").lower()
            
        if choice == 'y':
            number1 = result    
        elif choice == 'x':
            print("Thank you for using the calculator..")
            start_game = False
        else:
            os.system('cls')
            print("Starting new calculation")
            number1 = None

if __name__ == '__main__':
    main()       
            
        
        