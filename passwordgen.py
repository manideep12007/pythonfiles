import random
import string
def generate_password(length=12):
    if length < 8:
        raise ValueError("minimum length should be 8 characters for password")
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    symbols = '@#$%&*' #string.punctuation
    digits = string.digits
    
    #first character should be captail
    first_char = random.choice(upper_case)

    #last three characters should be in combination symbols and digits
    last_char = ''
    for _ in range(3):
        last_char += random.choice(digits+symbols)
    #rem_char is middle of the password

    #remaining length will be lowercase letters
    remaining_length = length - 4
    rem_char =''
    for _ in range(remaining_length):
        rem_char += random.choice(lower_case)
    
    full_password = first_char + rem_char + last_char
    return full_password

print(generate_password())
print()
print(generate_password(15))