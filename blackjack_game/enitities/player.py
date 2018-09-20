import itertools


class Player():
    def __init__(self, hand):
        self._cards = hand
        self._total_card_value = self._get_hand_value()
        self._number_of_aces = 0
        self._player_chips = 100

    def add_card(self, card):
        if card.rank == 'Ace':
            if (self._total_card_value + card.value > 21):
                card.value = 1
        self._cards.append(card)
        self._total_card_value = self._get_hand_value()

    def adjust_for_ace(self):
        pass

    def show(self):
        cards = list(
            map(lambda c: str(c) + ' (' + str(c.value) + ')', self._cards))
        print('YOUR CARDS ARE:\n' + ',\n'.join(cards) + '\n')

    def place_bet(self):
        bet_to_place = 0
        while bet_to_place is 0:
            _ = input('What is your bet: ')
            try:
                _ = int(_)
                if _ <= self._player_chips:
                    bet_to_place = _
                    print('---------')
                    break
                else:
                    print(
                        f'You cannot place a better higher than your chip value (you have {self._player_chips})\n'
                    )
            except:
                print('Please input a valid number.\n')
                continue

        self._propogate_bet(bet_to_place)
        return bet_to_place

    def _propogate_bet(self, bet_amount):
        self._player_chips -= bet_amount

    def _get_hand_value(self):
        cards = list(map(lambda c: int(c.value), self._cards))
        return sum(cards)


class AI(Player):
    def __init__(self, hand):
        super()
        self.card_was_seen = False
        self._cards = hand
        self._total_card_value = self._get_hand_value()
        self._number_of_aces = 0
        self._player_chips = 100

    def show(self):
        cards = list(
            map(lambda c: str(c) + ' (' + str(c.value) + ')', self._cards))
        cards[-1] = '[SECRET CARD]'
        print('THE DEALER CARDS ARE:\n' + ',\n'.join(cards) + '\n')

    