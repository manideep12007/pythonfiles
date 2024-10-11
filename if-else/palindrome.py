number = int(input('number : '))
temp_n = number
reverse_n = 0
while temp_n > 0:
    digit = temp_n % 10
    reverse_n = reverse_n*10 + digit
    temp_n = temp_n//10
if reverse_n == number:
    print(f"{number} is palindrome!")
else:
    print(f"{number} is not palindrome!")
