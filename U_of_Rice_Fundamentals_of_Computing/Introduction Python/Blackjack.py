# Mini-project #6 - Blackjack
__author__ = 'Linghuan'

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_front = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        global card_images
        
        if card_images == card_front:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            
        else:
            card_loc = (CARD_CENTER[0], 
                        CARD_CENTER[1])
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        
# define hand class
        
class Hand:
    def __init__(self):
        self.inventory = []

    def __str__(self):
        return "Hand contains:" + " ".join(str(card) for card in self.inventory)
        

    def add_card(self, card):
        self.inventory.append(card.suit+card.rank)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        
        value = 0 
        
        for card in self.inventory:
            value += VALUES[card[1:]]
        
        for card in self.inventory:
            if card[1:] == 'A':
                value += 10
                if value > 21:
                    value -= 10
                
        return value    
   
    def draw(self, canvas, pos):
        global card_images
        
        for card in self.inventory:
            card_new = Card(card[0], card[1])
            pos = list(pos)
            pos[0] = 10
            pos[0] += (self.inventory.index(card)*75)
            card_new.draw(canvas, pos)
            
            if card_images == card_back:
                
                card_images = card_front
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.inventory = []
        
        for suit in SUITS:
            for rank in RANKS:
                self.inventory.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.inventory)   # use random.shuffle()

    def deal_card(self):
        deck_remove = self.inventory[0]
        
        self.inventory.remove(deck_remove)
        
        return deck_remove	# deal a card object from the deck
    
    def __str__(self):
         return "Deck contains:" + " ".join(str(card) for card in self.inventory)	# return a string representing the deck
           

#define event handlers for buttons
def deal():
    global outcome, message, score, in_play, player, dealer, deck
    
    deck = Deck()

    deck.shuffle()

    player = Hand()

    player.add_card(deck.deal_card())

    deck.shuffle()

    player.add_card(deck.deal_card())

    print "Player" + str(player)

    deck.shuffle()

    dealer = Hand()

    dealer.add_card(deck.deal_card())

    deck.shuffle()

    dealer.add_card(deck.deal_card())

    print "Dealer" + str(dealer)

    message = "Hit or stand?"
    
    if in_play == True:
        
        score -= 1

    in_play = True
    
    outcome = ""
    

def hit():
    global outcome, message, score, in_play, player, dealer, deck
    
    if in_play == True:
        
         # if the hand is in play, hit the player
    
        if player.get_value() <= 21:

            player.add_card(deck.deal_card())

        # if busted, assign a message to outcome, update in_play and score

        if player.get_value() > 21: 

            message = "You went bust and lose"

            in_play = False

            score -= 1

        
def stand():
    global outcome, message, score, in_play, player, dealer, deck, score
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
 
    if in_play == True:
        
        if player.get_value() > 21:
            
            outcome = "You went bust and lose"
            
            in_play = False  
            
            score -= 1
        
        while dealer.get_value() < 17:
            
            dealer.add_card(deck.deal_card())  
                
    
    # assign a message to outcome, update in_play and score
    
    
        if dealer.get_value() <= 21:
            
            if player.get_value() > dealer.get_value():

                outcome = "You win"
                
                message = "New deal?"
                
                score += 1

            else:

                outcome = "You lose"
                
                message = "New deal?"
                
                score -= 1

        else:
            
            outcome = "You win"
            
            message = "New deal?"
            
            score += 1
            
        in_play = False
        

# draw handler    
def draw(canvas):
    global in_play, card_images
    
    if in_play == True:
        
        card_images = card_back
    
    dealer.draw(canvas, (0, 170))
    player.draw(canvas, (0, 400))
    
    canvas.draw_text('Dealer', (50, 120), 40, 'Black')
    canvas.draw_text('Player', (50, 350), 40, 'Black')
    #canvas.draw_text('Value: ' + str(dealer.get_value()), (200, 120), 20, 'Black')
    #canvas.draw_text('Value: ' + str(player.get_value()), (450, 350), 20, 'Black')
    
    
    canvas.draw_text(outcome, (200, 310), 35, 'Red')
    canvas.draw_text(message, (200, 350), 35, 'Red')
    
    canvas.draw_text('Blackjack', (120, 50), 50, 'Blue')
    canvas.draw_text('Score: '+str(score), (400, 50), 40, 'Red')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()

frame.start()


# remember to review the grading rubric