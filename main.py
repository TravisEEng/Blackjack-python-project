############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.




from art import logo 
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand  = []
player_hand = []

def prompt_to_play():
    startGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    return startGame

def start_game():
    print(logo)
    prepare_game()
    initial_deal()


def prepare_game():
    global player_hand
    global dealer_hand
    player_hand = []
    dealer_hand = []

def initial_deal():
    draw_cards(2,"dealer")
    draw_cards(2,"player")
    display_hands()   
  
  
def draw_cards(num_of_draws,user):
    for card in range(num_of_draws):
        card = random.choice(cards)
        if(user == "player"):
            player_hand.append(card)
        else:
            dealer_hand.append(card)

def sum_of_deck(user):
    if(user == "player"):
        return sum(player_hand)
    else:
        return sum(dealer_hand)

def display_hands():
    print(f"Your cards: {player_hand}, current score: {sum_of_deck('player')}")    
    print(f"Computer's first card: {dealer_hand[0]}")
      

def play_again():
    restart = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    return restart
    
def check_for_loser():
    if(sum_of_deck("player") > 21 and sum_of_deck("dealer") > 21):
        return("draw")
    if(sum_of_deck("player") > 21):
        return("playerloss")
    if(sum_of_deck("dealer") > 21):
        return("dealerloss")
    
    return ""

def you_went_over():
    display_final_hands()
    print('You went over. You lose 😭')

def computer_went_over():
    display_final_hands()
    print('Opponent went over. You win 😁')

def draw():
    print('Draw')
           
 
def display_final_hands():
    print(f"Your final hand: {player_hand}, final score: {sum_of_deck('player')}")    
    print(f"Computer's final hand: {dealer_hand}, final score: {sum_of_deck('dealer')}") 

def dealer_solo_draws():
    draw_cards(1,"dealer")
        
def determine_winner():
    #check both hands
    display_final_hands()
    if(sum_of_deck("player") > sum_of_deck("dealer")):
        player_wins_through_score()
    elif(sum_of_deck("player") == sum_of_deck("dealer")):
        draw()
    else:
        computer_wins_through_score()

def computer_wins_through_score():
    print('You lose 😤')

def player_wins_through_score():
    print('You win 😃')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

playing_game = prompt_to_play()
end_game = False
if (playing_game == "y"):
    while(playing_game == "y"):
        clearConsole()
        start_game()
        pass_or_draw = input("Type 'y' to get another card, type 'n' to pass: ")
        while(pass_or_draw=="y"):
            draw_cards(1,"player")
            draw_cards(1,"dealer")
            display_hands()
            has_gone_over = check_for_loser()
            if(has_gone_over != ""):
                if(has_gone_over=="playerloss"):
                    you_went_over()
                    end_game = True
                    break
                elif(has_gone_over=="dealerloss"):
                    computer_went_over()
                    end_game = True
                    break
                else:
                    display_final_hands()
                    end_game = True
                    draw()
                    break
            pass_or_draw = input("Type 'y' to get another card, type 'n' to pass: ")

        dealer_solo_draws()
        #check if gone over
        # no one has gone over, so check if dealer has
        dealer_gone_over = check_for_loser()
        if(end_game == False):     
            if(dealer_gone_over=="dealerloss"):
                computer_went_over()
            else:
                determine_winner()
            
        playing_game = play_again()
    
        

    

