from urllib import response
from deck import Deck
from hand import Hand
import os
import time

class Player:
    '''A game player.'''
    def __init__(self, name="player1", score=0):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name} Score: {self.score}"

class Game:
    '''A parent class to use for all Games.'''
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
            response = input(question)[0].lower()
        return response

    def ask_for_number(self, question, low, high):
        response = None
        while response not in range(low, high):
            try:
                response = int(input(question))
            except:
                print("{response} is not an integer between {low} and {high}.")
        return response

class CardGame(Game):
    '''A parent class to use for all Card Games.'''
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class CardPlayer(Hand, Player):
    '''A card game player.
        inherites from Hand and Player'''
    def __init__(self, name):
        Hand.__init__(self, name)
        Player.__init__(self, name)
        
    def __str__(self):
        return Player.__str__(self)