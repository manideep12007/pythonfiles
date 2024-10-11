import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def set_diffculty(level):
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
    
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low..")
        return attempts -1
    elif guessed_number > answer:
        print("Your guess is too high..")
        return attempts -1
    else:
        print(f'Your answer is right.. The answer was {answer}')
        print("You won the game...")
        
def main():
    print("Let me think of a number between 1 to 50.")
    answer = random.randint(1,50)
    #print(answer)
    level = input("Choose your level easy or hard ? \n").lower()
    while level not in ['easy','hard']:
        print("sorry we do not have that level select easy/hard")
        level = input("Choose your level easy or hard ?").lower()
    attempts = set_diffculty(level)
    guessed_number = 0
    while answer != guessed_number:
        print(f"You have {attempts} attempts remaining to guess the number...")
        guessed_number = int(input("Guess the number : "))
        attempts = check_answer(guessed_number,answer,attempts)
        if attempts == 0:
            print("You are out of guesses... You loose!")
            return 
        elif guessed_number != answer:
            print("Guess again!...")
        else:
            return 

if __name__ == '__main__':
    main()
    




    