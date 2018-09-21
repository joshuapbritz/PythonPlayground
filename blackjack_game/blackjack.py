from enitities import player, deck, pool


class Game():
    def __init__(self):
        self.playing = True
        self.pool = pool.Pool()

        self.play_game()

    def player_play(self):
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
                    print(
                        f'BUST! Your total was {self.player._total_card_value}'
                    )
                    self.pool.reset()
                    break
            elif player_move == '2':
                playing = False
                break
            else:
                print('Please hit (1) or stand (2)')
                continue

    def ai_play(self):
        playing = True
        while playing:
            if self.ai.card_was_seen == False:
                self.ai.card_was_seen = True
            else:
                new_card = self.deck.hit()
                self.ai.add_card(new_card)

            value = self.ai._total_card_value
            if value > 21:
                self.player._player_chips += self.pool.get()
                self.pool.reset()
                print(
                    f'Dealer has bust. You win. You have {self.player._player_chips} chips'
                )
                break
            elif value >= 17 and value <= 21:
                message_start = f"The dealer's score is {value}. Your score is {self.player._total_card_value}"
                if value > self.player._total_card_value:
                    print(
                        f"{message_start}. You lose. You have {self.player._player_chips} chips"
                    )
                else:
                    self.player._player_chips += self.pool.get()
                    self.pool.reset()
                    print(
                        f"{message_start}. You win, You have {self.player._player_chips} chips"
                    )
                break
            print(value)

    def play_game(self):
        while self.playing:
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
            self.pool.add(self.player.place_bet())

            self.ai.show()
            self.player.show()
            
            self.player_play()
            self.ai_play()

            play_again = None

            while play_again is None:
                result = input('Try again?')

                if result == '1' or result == '2':
                    play_again = result == '1'
            
            if play_again:
                continue
            else:
                print('Thank you for playing')
                self.playing = False


game = Game()
