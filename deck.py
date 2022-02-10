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
        # number_of_cards = len(self.cards) # Don't assume there are 52
        # for i in range(number_of_cards):
        #     j = rng.randrange(i, number_of_cards)
        #     (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])
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