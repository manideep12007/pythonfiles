
import string
lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase
def encryption_char(char,shift_key):     
    if char in lower_case_letters:
        new_position = (lower_case_letters.index(char)+shift_key)%26
        return lower_case_letters[new_position]
    elif char in upper_case_letters:
        new_position = (upper_case_letters.index(char)+shift_key)%26
        return upper_case_letters[new_position]
    else:
        return char
def decryption_char(char,left_shift):
    
    if char in lower_case_letters:
        new_position = (lower_case_letters.index(char)-left_shift)%26
        return lower_case_letters[new_position]
    elif char in upper_case_letters:
        new_position = (upper_case_letters.index(char)-left_shift)%26
        return upper_case_letters[new_position]
    else:
        return char
def encryption(plain_text,shift_key):  
    cipher_text = ''.join(encryption_char(char,shift_key) for char in plain_text)
    print("Here the text after encryption : ")
    print(cipher_text)
def decryption(cipher_text,left_shift): 
    decrypt_text = ''.join(decryption_char(char,left_shift) for char in cipher_text)
    print("Here the text after decryption : ")
    print(decrypt_text)  
def main():    
    game_start = True
    while game_start:
        what_to_do = input("Type e for encryption and d for decryption :\n").lower()
        while what_to_do not in ['e','d']:  
            print("please select valid inputs e = encryption and d = decryption")
            what_to_do = input("Type e for encryption and d for decryption :\n").lower()   
        text = input('Type your message :\n')
        shift = int(input('Enter shift key :\n'))     
        if what_to_do == 'e':    
            encryption(plain_text=text,shift_key=shift)
        else:           
            decryption(cipher_text=text,left_shift=shift)
        choice = input("Do you want to continue again ? (y/n) ").lower()   
        while choice not in ['y','n']:       
            print("Please select valid inputs yes (y) or no (n) ")
            choice = input("Do you want to continue again ? (y/n) ").lower()          
        if choice == 'y':        
            game_start = True
            main()       
        else:  
            game_start = False                
            print("Good bye!") 
            break           
if __name__ == '__main__':
    print(" Welcome to ENCRYPTION AND DECRYPTION game ")
    main()
    
    