import itertools

class Player():
    def __init__(self, hand):
        self._cards = hand
        self._total_card_value = self._get_hand_value()
        self._number_of_aces = 0
    
    def add_card(self, card):
        pass
    
    def adjust_for_ace(self):
        pass
    
    def show(self):
        cards = list(map(lambda c: str(c) + ' (' + str(c.value) + ')', self._cards))
        print('YOUR CARDS ARE:\n' + ',\n'.join(cards) + '\n')

    def _get_hand_value(self):
        cards = list(map(lambda c: int(c.value), self._cards))
        return sum(cards)

class AI(Player):
    def show(self):
        cards = list(map(lambda c: str(c) + ' (' + str(c.value) + ')', self._cards))
        cards[-1] = 'XXX\nXXX\nXXX'
        print('THE DEALER CARDS ARE:\n' + ',\n'.join(cards) + '\n')