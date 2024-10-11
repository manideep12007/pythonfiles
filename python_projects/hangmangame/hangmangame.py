
import words
import random
import stages

def choosen_word():
    
    """Randomly choosing a word from the list"""
    choose_word = random.choice(words.words)
    return choose_word

def guess_letter():
    
    """user to enter a letter """
    _lett = input("enter your guessed letter : ").lower()
    return _lett


def main():
    
    """Main game starts with settling all requirements below"""
    
    lives = 5
    stage = stages.stages
    game_over = False
    
    #choosing a word from words list
    choosen = choosen_word()
    #print(choosen)
    
    #creating display_board based on choosen word
    display_board = []
    for _ in range(len(choosen)):
        display_board += '_'
    print("Player your display board : ",display_board)
    
    #actual game begins
    while not game_over:
        
        #guessing a letter by player
        guess = guess_letter()
        
        #checks if guess was in choosen word
        if guess in choosen:
            for position in range(len(choosen)):
                if choosen[position] == guess:
                    display_board[position] = guess
            print(f"You guess correctly ! {"".join(display_board)}")
        else:
            lives -= 1
            print("Wrong guess! you lost one live")
            print(f"you got {lives}")
            print(stage[lives])
        
        #check for win or lose condition
        if '_' not in display_board:
            game_over = True
            print("You win!")
            print(f'Game completed you guessed {choosen} word')
        elif lives==0:
            game_over = True
            print(f'Game over your lives finished you could not guessed {choosen} word')
          
        #asking for playing again  
        while game_over:
            other_game = input("enter yes or no to start game agin (y/n) : ").upper()
            while other_game not in ['Y','N']:
                print("select correctly y/n only")
                other_game = input("enter yes or no to start game agin (y/n) : ").upper()
            if other_game == 'Y':
                game_over = False
                main()
            else:
                print("Thanks for playing")
                break

#game execution 
if __name__ == '__main__':
    main()