class Card:
    '''Represents a playing card.
        Attributes: suit and rank'''

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = [" ", "Ace", "2", "3", "4", "5", "6", "7", "8",
            "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.ranks[self.rank]} of {self.suits[self.suit]}"

    def compare(self, other):
        '''Compares the suit then the rank of the current card
            against another card.'''
        # Check suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits must be the same... check ranks now
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
        return 0
        
    # These methods overload ==, !=, <=, >=, <, and > operators
    def __eq__(self, other):
        return self.compare(other) == 0
    def __ne__(self, other):
        return self.compare(other) != 0
    def __le__(self, other):
        return self.compare(other) <= 0
    def __ge__(self, other):
        return self.compare(other) >= 0
    def __lt__(self, other):
        return self.compare(other) < 0
    def __gt__(self, other):
        return self.compare(other) > 0

if __name__ == "__main__":
    card1 = Card(1, 13)
    print(card1)
    
    card2 = Card(1, 1)
    print(card2)
    
    print(Card.suits[1]) # access a class attribute directly
    
    card3 = Card(1, 11)
    
    print(f"{card1} less than {card2}? {card1 < card2}") # False
    print(f"{card1} greater than {card2}? {card1 > card2}") # True
    print(f"{card1} equal to {card3}? {card1 == card3}") # True