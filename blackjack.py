from game import *

class BlackJackCard(Card):
    '''A playing card for a BlackJack game.'''
    ACE_VALUE = 1

    def __init__(self, suit, rank, face_up=True):
        '''Initializes a BlackJack Card.'''
        Card.__init__(self, suit, rank)
        self.is_face_up = face_up

    def __str__(self):
        '''Displays a BlackJack Card.'''
        if self.is_face_up:
            return Card.__str__(self)
        else:
            return "X of X"

    def flip(self):
        '''Flips a card over.'''
        self.is_face_up = not self.is_face_up

    # Decorators modify the behavior of a method. The @property decorator allows a callable method to behave as if it were an instance attribute.
    @property 
    def value(self):
        '''Returns a numeric value for all cards ranks'''
        if self.is_face_up:
            n = self.rank
            if n > 10:
                n = 10
        else:
            n = None
        return n

class BlackJackDeck(Deck):
    '''A Deck of cards for a BlackJack game.'''
    def __init__(self):
        '''Initializes a deck of BlackJack Cards'''
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = BlackJackCard(suit, rank)
                self.cards.append(card)

    def reload(self):
        '''Reloads the BlackJackDeck then shuffles the cards.'''
        self.__init__()
        self.shuffle()

class BlackJackHand(CardPlayer):

    def __str__(self):
        return f"{self.name}:\n{Deck.__str__(self)}Total: {self.total}\n"

    def reset(self):
        self.__init__(self.name)

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        total = 0
        hand_has_an_ace = False
        for card in self.cards:
            total += card.value
            if card.value == BlackJackCard.ACE_VALUE:
                hand_has_an_ace = True

        if hand_has_an_ace and total <= 11:
            total += 10

        return total

    def is_busted(self):
        '''Has the player's card total exceeded 21?'''
        return self.total > 21

    def bust(self):
        '''The hand's card total has exceeded 21.'''
        print(f"{self.name}, busts.")
        self.lose()

    def lose(self):
        print(f"{self.name}, loses.\n")

    def win(self):
        print(f"{self.name}, wins.\n")




class BlackJackPlayer(BlackJackHand):
    '''A player's hand of cards for a BlackJack game.'''

    def is_hitting(self):
        '''Ask if the player wants another card.'''
        question = f"{self.name} do you want a hit? (Y/N): "
        response = Game().ask_yes_no(question)
        return response == 'y'

    def push(self):
        '''Player ties with the dealer.'''
        print(f"{self.name}, pushes.")


class BlackJackDealer(BlackJackHand):
    '''The dealer's hand of cards for a BlackJack game.'''

    def is_hitting(self):
        '''Dealer takes another card as long as card total is below 17.'''
        return self.total < 17

    def flip_first_card(self):
        '''The dealer's card flips over.'''
        self.cards[0].flip()
    

class BlackJack(CardGame):
    '''A BlackJack game.'''
    def __init__(self):
        '''Initialize a new BlackJack game.'''
        self.deck = BlackJackDeck()
        self.deck.shuffle()
        self.clear()
        # create players with names
        self.players = []
        self.player_count = self.ask_for_number("How many players? (1 - 5): ", 1, 5)
        for i in range(1, self.player_count + 1):
            name = ''
            while name == '':
                name = input(f"Enter name for player {i}: ")
                if name != '':
                    self.players.append(BlackJackPlayer(name))

        self.dealer = BlackJackDealer("dealer")

    @property
    def still_playing(self):
        '''Return a list of player's that have not yet busted.'''
        whos_still_playing = []
        for player in self.players:
            if not player.is_busted():
                whos_still_playing.append(player)
        return whos_still_playing

    def additional_card(self, player):
        '''Deal one or more cards to a player.'''
        while not player.is_busted() and player.is_hitting():
            self.deck.deal((player, ), 1)
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        '''Start the game.'''
        self.clear()

        # deal the initial cards
        self.deck.deal(self.players + [self.dealer], 2 * (self.player_count + 1))
        for player in self.players:
            print(player)
        self.dealer.flip_first_card() # hide dealer's first card
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.additional_card(player)

        self.dealer.flip_first_card() # reveal dealer's first card

        # dealer has either won or takes additional cards
        if not self.still_playing:
            print(self.dealer) # dealer has won
            print("Dealer wins.")
        else:
            print(self.dealer)
            self.additional_card(self.dealer) # dealer hits

            # check for win, lose, or push
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # reset the game
        for player in self.players:
            player.reset()
        self.dealer.reset()
        self.deck.reload()
        input("Game over. Press any key to continue...")
        self.clear()

def start():
    game = BlackJack()
    play_again = True
    while play_again:
        game.clear()
        game.play()
        response = game.ask_yes_no("\nDo you wish to play again? (Y/N) ")
        if response != 'y':
            play_again = False
    print('Thanks for playing.')
    game.pause(2)
    game.clear()

if __name__ == "__main__":
    start()