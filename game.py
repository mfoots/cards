import os
import time
from card import Card
from deck import Deck
from hand import Hand

class Player:
    '''A game player.'''
    def __init__(self, name="player1", score=0):
        self.name = name.title()
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"

class Game:
    '''A Game.'''
    def __init__(self, title=""):
        self.title = title

    def pause(self, duration=1):
        time.sleep(duration)

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def ask_yes_no(self, question):
        response = None
        while response not in ('y', 'n'):
            response = input(question).lower()[0]
        return response

    def ask_for_number(self, question, low, high):
        response = None
        while response not in range(low, high):
            try:
                response = int(input(question))
            except:
                print("{response} is not an integer between {low} and {high}.")
        return response

class CardPlayer(Hand, Player):
    '''A card game player.'''
    def __init__(self, name):
        Hand.__init__(self, name)
        Player.__init__(self, name)
        
    def __str__(self):
        return Player.__str__(self)

class CardGame(Game):
    '''A Card Game.'''
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
