from deck import Deck
import os
import time

class CardGame:
    '''The parent class to use for all game classes.'''
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def pause(self, duration=1):
        time.sleep(duration)

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        

