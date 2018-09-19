from enitities import player, deck, pool


class Game():
    def __init__(self):
        self.pool = pool.Pool()
        # Create a deck instance
        self.deck = deck.Deck()

        # Shuffle the deck for the game
        self.deck.shuffle()

        # Deal the cards
        dealt_cards = self.deck.deal()

        # Give the players there cards
        self.ai = player.AI(dealt_cards.get('ai'))
        self.player = player.Player(dealt_cards.get('player'))

        # Allow the player to place a bet
        self.player.place_bet()

        self.ai.show()
        self.player.show()

        self.player_hit_or_stand()

    def player_hit_or_stand(self):
        playing = True
        while playing:
            player_move = input('Hit (1) or Stand (2)? ')

            new_card = self.deck.hit()

            if player_move == '1':
                self.player.add_card(new_card)
                self.ai.show()
                self.player.show()
                if self.player._total_card_value <= 21:
                    pass
                else:
                    print('You busted')
                    self.pool.reset()
                    break
            elif player_move == '2':
                playing = False
                break
            else:
                print('Please hit (1) or stand (2)')
                continue

    def ai_play(self):
        pass


game = Game()
