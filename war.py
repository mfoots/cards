from game import *

class WarGame(CardGame):
    def __init__(self):
        CardGame.__init__(self)
        self.computer = CardPlayer("Computer")
        self.player = CardPlayer("Human")
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
        print(f"{self.computer} \t{self.player}")
        
    def play(self, rounds=26):
        self.intro()
        
        while self.round <= rounds and self.player.cards != []:
            print(f"Round: {self.round}")
            computer_card = self.computer.pop()
            player_card = self.player.pop()
            print(f"{self.computer.name}: {computer_card}\n{self.player.name}: {player_card}")
            if computer_card > player_card:
                print(f"{self.computer.name} wins!")
                self.computer.score += 1
            elif player_card > computer_card:
                print(f"{self.player.name} wins!")
                self.player.score += 1
            else:
                print("It's a draw!")

            print("\nCurrent Scores:")
            self.status()
            
            self.pause()
            self.clear()
            self.round += 1
            
        print("Final Scores:")
        self.status()
        self.pause()
        print("\nGame over.\n")

if __name__ == "__main__":
    game = WarGame()
    again = True
    while again == True:
        game.clear()
        rounds = game.ask_for_number("How many rounds would you like to play? ", 1, 26)
        game.play(rounds)
        game.clear()
        again = 'y' == game.ask_yes_no("Do you want to play again (Yes or No)? ")
    
    game.clear()
    print("Thank's for playing!\n")