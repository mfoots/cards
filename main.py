import os
import time
from card import Card
from deck import Deck
from hand import Hand

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def test1():
    card1 = Card(1, 13)
    print(card1)
    
    card2 = Card(1, 1)
    print(card2)
    
    print(Card.suits[1]) # access a class attribute directly
    
    card3 = Card(1, 11)
    
    print(f"{card1} less than {card2}? {card1 < card2}") # False
    print(f"{card1} greater than {card2}? {card1 > card2}") # True
    print(f"{card1} equal to {card3}? {card1 == card3}") # True

def test2():
    
    red_deck = Deck()
    print(red_deck)
    
    blue_deck = Deck()
    blue_deck.shuffle()
    print(blue_deck)

def test3():
    deck = Deck()
    deck.shuffle()
    
    hand1 = Hand('Joe')
    hand2 = Hand('Gordon')
    
    print('Player hands...\n')
    time.sleep(1)
    print(hand1)
    time.sleep(1)
    print(hand2)
    time.sleep(2)
    clear()
    
    print('Dealing cards to each hand...\n')
    time.sleep(2)
    deck.deal((hand1, hand2), 10)
    clear()
    
    print('Displaying hands...\n')
    time.sleep(1)
    print(hand2)
    time.sleep(1)
    print(hand1)

    # check how many cards are left
    print(f"{len(deck.cards)} cards remain in the deck.\n") 

clear()
test3()