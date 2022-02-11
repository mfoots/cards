from deck import Deck

# Hand inherits from Deck
class Hand(Deck):
    '''Represents a hand of playing cards.'''

    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        '''Adds a new Card to the Hand'''
        self.cards.append(card)

    def __str__(self):
        '''Overrides the __str__ method of the Deck class'''
        s = f"Hand: {self.name}"
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        # return statement also calls the __str__ mothod of the parent class
        return s + Deck.__str__(self)
    