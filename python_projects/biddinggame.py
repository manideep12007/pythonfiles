
''' 
The highest bidder wins 
'''

import os
import pandas

def add_name_and_bid(name,bid,bidding_data):
    bidding_data[name] = bid
    return bidding_data

def find_winner(bidding_data):
    highest_bid = 0
    winner_of_bid = ''
    for bidder in bidding_data:
        bidder_bid = bidding_data[bidder]
        if bidder_bid > highest_bid:
            highest_bid = bidder_bid
            winner_of_bid = bidder
    return f'The winner of the cuurent bid is : {winner_of_bid}\nAnd the bid of {highest_bid} rupees'

bidder_data = {}
end_of_bid = False

while not end_of_bid:
    
    print("---WELCOME TO BIDDING GAME---")
    name = input("What is your name? : ")
    bid = float(input('How much bid do you put on ? : '))
    data_set_bidd = add_name_and_bid(name,bid,bidder_data)
    data_set = pandas.DataFrame(list(data_set_bidd.items()),columns=['bidder',bid])
    data_set.index += 1
    
    any_other_bidders = input('Is any other bidders ? (y/n) : ')
    while any_other_bidders not in {'y','n'}:
        print("enter valid inputs yes y or no n ")
        any_other_bidders = input('Is any other bidders ? (y/n) : ')
    
    if any_other_bidders == 'n':
        end_of_bid = True
        print("\nCurrent Bids: ")
        print(data_set) 
        print()
        winner = find_winner(bidder_data)
        print(winner)
    else:
        os.system('cls')
        
        