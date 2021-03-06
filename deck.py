from card import Card

class Deck:
    '''Represents a deck of playing cards.'''
                
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))
                
    def __str__(self):
        s = "" # accumulator variable
        for card in self.cards:
            s += f"{card}\n"
        return s

    def shuffle(self):
        import random
        rng = random.Random() # Creates a random number generator
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    # do this after creating the Hand class

    def deal(self, hands, number_of_cards=999):
        '''Deals one or more cards to one or more Hand objects'''
        number_of_hands = len(hands)
        for i in range(number_of_cards):
            if self.is_empty():
                # are all the cards gone?
                break
            # take the top card
            card = self.pop()
            # whose turn is next (mod makes it wrap around)
            hand = hands[i % number_of_hands]
            # add the card to the hand
            hand.add(card)

if __name__ == "__main__":
    red_deck = Deck()
    print(red_deck)
    
    blue_deck = Deck()
    blue_deck.shuffle()
    print(blue_deck)