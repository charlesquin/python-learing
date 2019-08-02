"""""
8/2/2019

Python code project. Functional but needs changes. 

Created during the "Complete Python Bootcamp: Go from zero to hero in Python 3" course

https://www.udemy.com/complete-python-bootcamp/

"""



import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit  

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
          

    def __str__(self):
        deck_comp = '' # start with an empty string
        for card in self.deck:
            deck_comp +=  '\n ' +card.__str__() 
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self): 
        single_card = self.deck.pop()
        return single_card


class Hand():

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def __str__(self): 
        return [str(i) for i in self.cards]
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 


class Chips:    

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet():
    
    while True:
        try:
            player_chips.bet = int(input("What is your bet? "))
            if player_chips.total >= player_chips.bet:
                print(f'Placing a {player_chips.bet} chip bet')
                break
            else:
                print("Not enough chips. Try another bet.")
                continue
                
        except ValueError:
            print("That is not a number amount. ")

            continue


def hit(deck,hand):

    hand.add_card(deck.deal()) 
    hand.adjust_for_ace()
    

def hit_or_stand(deck,hand):
    
    global playing
    player_decision = input("Hit or Stand? ")
    if player_decision[0].lower() == 'h':
        hit(deck,hand)
        playing = True # Player hits
    else:
        playing = False  # Player Stands


def show_some(player,dealer): 
    print("Player cards: {}.".format(', '.join(player.__str__())))
    print("Dealer cards: {}, [Card Hidden]".format(', '.join(dealer.__str__()[:1])))


def show_all(player,dealer):
    print("Player cards: {}. The card value is: {}".format(', '.join(player.__str__()),player.value))
    print("Dealer cards: {}. The card value is: {}".format(', '.join(dealer.__str__()),dealer.value))


def player_busts(dealer,player,chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(dealer,player,chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(dealer,player,chips):
    print("Dealer busts!")
    chips.win_bet()

    
def dealer_wins(dealer,player,chips):
    print("Dealer wins!")
    chips.lose_bet()

    
def push():
    print("Player and dealer tie! Bust!")


while True:
    
    # Print an opening statement
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("       Welcome to Blackjack!       ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    
    # Create & shuffle the deck, deal two cards to each player
    playing_deck = Deck()
    playing_deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(playing_deck.deal())
    player.add_card(playing_deck.deal())
    dealer.add_card(playing_deck.deal())
    dealer.add_card(playing_deck.deal())    
        
    # Set up the Player's chips
    player_chips = Chips()
    print(f'Player has {player_chips.total} total chips')    
    
    # Prompt the Player for their bet
    take_bet()
    
    # Show cards (but keep one dealer card hidden)
    print("Dealing the cards!")
    show_some(player,dealer)
    
    playing = True   
    
    while playing:  # recall this variable from our hit_or_stand function
    
        # Prompt for Player to Hit or Stand
    
        hit_or_stand(playing_deck,player)
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        
    
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,dealer,player_chips)
            playing = False
            break
        else:
            pass            
            

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while player.value <22 and dealer.value < 17:
            print("Dealing card to dealer.")
            dealer.add_card(playing_deck.deal())
            
                
        show_all(player,dealer)   # Show all cards

        if dealer.value == 21 and player.value !=21:
            dealer_wins(dealer,player,player_chips)
            break
        elif dealer.value >21 and player.value <=21:
            dealer_busts(dealer,player,player_chips)
            break
        elif dealer.value < player.value:
            player_wins(dealer,player,player_chips)
            break
        elif player.value == 21:
            player_wins(dealer,player,player_chips)
            break
        else:
            print(f'{player.value} + {dealer.value}')

    # Inform Player of their chips total 
    print(f'{player_chips.total} total chips')
    

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break