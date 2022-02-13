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

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    
    hand1 = Hand('Joe')
    hand2 = Hand('Gordon')
    
    print('Creating player hands...\n')
    print(hand1)
    print(hand2)
    
    print('Dealing cards to each hand...\n')
    deck.deal((hand1, hand2), 10)
    
    print('Displaying hands...\n')
    print(hand2)
    print(hand1)

    # check how many cards are left
    print(f"{len(deck.cards)} cards remain in the deck.\n")