from card import Card
from deck import Deck

def test():
    card1 = Card(1, 13)
    print(card1)
    
    card2 = Card(1, 1)
    print(card2)
    
    print(Card.suits[1]) # access a class attribute directly
    
    card3 = Card(1, 11)
    
    print(f"{card1} less than {card2}? {card1 < card2}") # False
    print(f"{card1} greater than {card2}? {card1 > card2}") # True
    print(f"{card1} equal to {card3}? {card1 == card3}") # True
    
    # print("\nRed Deck")
    
    red_deck = Deck()
    # print(red_deck)
    
    # print("\nBlue Deck (Shuffled)")
    blue_deck = Deck()
    blue_deck.shuffle()
    # print(blue_deck)


test()