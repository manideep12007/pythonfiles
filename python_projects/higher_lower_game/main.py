import dataset
import random
import gameart
import os

print(gameart.game_logo)

def display_account_info(account):
    name = account["name"]
    description = account["description"]
    return f'{name},a {description}'

def follower_count(account):
    followers = account['followers']
    return followers

def check_guess(guess,follower1,follower2):
    if follower1 < follower2:
        return guess == 2
    else:
        return guess == 1
def main():
    score = 0
    account_1 = random.choice(dataset.celebrities)
    while True:
        account_2 = random.choice(dataset.celebrities)
        while account_1 == account_2:
            account_2 = random.choice(dataset.celebrities)
             
        print(f"Compare 1: {display_account_info(account_1)}")
        print(gameart.vs)
        print(f"Compare 2: {display_account_info(account_2)}")
        
        guess = int(input("Who has more followers ? Type 1 or 2 :  "))
        while guess not in [1,2]:
            print("Guess only 1 or 2")
            guess = int(input("Who has more followers ? Type 1 or 2 : "))
            
        follower_count_1 = follower_count(account_1)
        follower_count_2 = follower_count(account_2)
        
        is_correct = check_guess(guess,follower_count_1,follower_count_2)
        os.system('cls')
        print(gameart.game_logo)
        if is_correct:
            score += 1
            print(f'Your are right. Your score is: {score}')
            account_1 = account_1 if follower_count_1 >= follower_count_2 else account_2
        else:
            print(f'Your are Wrong. Your final score is: {score}')
            break 
            

if __name__ == '__main__':
    main()
    
    

    







