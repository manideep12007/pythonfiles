'''
Rock Paper Scissor game 

where Rock wins against Scissor
Where Scissor wins against Papper
where Paper wins against Rock

0 - Rock
1 - Paper
2 - Scissor

----------------------------------------------------
   user_choice     computer_choice       winner
----------------------------------------------------
|    0                0              Tied          |
|    0                1              Computer won  |
|    0                2              User won      |
|    1                0              User won      |
|    1                1              Tied          |
|    1                2              Computer won  |
|    2                0              Computer won  |
|    2                1              User won      |
|    2                2              Tied          |
----------------------------------------------------

OTHER THAN 0,1,2 WILL BE INVALID CASES

USER CONDITONS IF
1. COMPUTER_CHOICE > USER_CHOICE ->LOSE
2. USER_CHOICE > COMPUTER_CHOICE -> WIN
3. COMPUTER_CHOICE = 2 THEN USER_CHOICE = 0 -> USER WIN
4. COMPUTER_CHOICE = 0 THEN USER_CHOICE = 2 -> USER WIN
5. IF USER_CHOICE == COMPUTER_CHOICE -> DRAW
6. IF USER_CHOICE != [0,1,2] => INVALID
'''
import random

def get_user_choice():
    user_choice = int(input("Enter 0 for Rock\n1 for Paper\n2 for Scissors : "))
    return user_choice

def get_computer_choice():
    computer_choice = random.randint(0,2)
    return computer_choice

def display_choices(user_choice,computer_choice,game_images):
    print("User choice :",game_images[user_choice])
    print("Computer choice :",game_images[computer_choice])

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice :
        return "Match tied"
    elif user_choice == 0 and computer_choice == 2:
        return "You won Computer lose"
    elif user_choice == 2 and computer_choice == 0:
        return "You lose Computer won"
    elif user_choice > computer_choice:
        return "You lose Computer Won"
    elif user_choice < computer_choice:
        return "You win Computer lose"

def main():
    rock = "🪨"
    paper = "🧻"
    scissors = "✂️"
    game_images = [rock,paper,scissors]
    user_choice = get_user_choice()
    if user_choice not in [0,1,2]:
        print("User you entered out of box please enter only 0/1/2")
        return
    computer_choice = get_computer_choice()
    display_choices(user_choice,computer_choice,game_images)
    result = determine_winner(user_choice,computer_choice)
    print(result)
    choice = input("click Y for yes for next game\n N for exit game : ").capitalize()
    while choice not in ['y','Y','n','N']:
        print("please select choice may be y or n or Y or N")
        choice = input("click Y for yes for next game\n N for exit game : ").capitalize()
    if choice == 'Y':
        main()
    else:
        print("Thank you for playing!!..")
        
if __name__ == "__main__":
    main()
    
    