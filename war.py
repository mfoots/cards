from game import CardGame
from hand import Hand

class WarGame(CardGame):
    def __init__(self):
        CardGame.__init__(self)
        self.computer = Hand('Computer')
        self.player = Hand('Player')

        self.computer_score = 0
        self.player_score = 0
        self.round = 1

        self.deck.deal((self.computer, self.player), 52)

    def intro(self):
        self.clear()
        for i in range(1, 5):
            print("Welcome to the War Card Game!")
            progress = '.' * i
            print(f"Loading game{progress}")
            self.pause()
            self.clear()

    def status(self):
        print(f"Computer: {self.computer_score} \tPlayer: {self.player_score}")
        
    def play(self, rounds=26):
        self.intro()
        
        while self.round <= rounds and self.player.cards != []:
            print(f"Round: {self.round}")
            computer_card = self.computer.pop()
            player_card = self.player.pop()
            print(f"Computer: {computer_card}\nPlayer: {player_card}")
            if computer_card > player_card:
                print("Computer wins!")
                self.computer_score += 1
            elif player_card > computer_card:
                print("Player wins!")
                self.player_score += 1
            else:
                print("It's a draw!")

            print("\nCurrent Scores:")
            self.status()
            
            self.pause()
            self.clear()
            self.round += 1
            
        print("Final Scores:")
        self.status()

if __name__ == "__main__":
    game = WarGame()
    game.play(5)