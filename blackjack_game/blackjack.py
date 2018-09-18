from enitities import player, deck


class Game():
    def __init__(self):
        # Create a deck instance
        self.deck = deck.Deck()

        # Shuffle the deck for the game
        self.deck.shuffle()

        # Deal the cards
        hands = self.deck.deal()

        # Give the players there cards
        self.ai = player.AI(hands.get('ai'))
        self.player = player.Player(hands.get('player'))

        self.ai.show()

        self.player.show()

        

game = Game()
