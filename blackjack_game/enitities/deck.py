import numpy
import itertools

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}

class Card():
    def __init__(self, suit, rank, value):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank, values.get(rank)))

    def __str__(self):
        string_values = list(map(lambda v: str(v), self.cards))
        return str(string_values)

    def shuffle(self):
        for _ in range(4):
            self._do_shuffle()

    def deal(self):
        pass

    def _do_shuffle(self):
        '''
        Cuts and shuffles the deck
        '''

        cut_decks = [
            self.cards[0:13], self.cards[13:26], self.cards[26:39],
            self.cards[39:52]
        ]

        numpy.random.shuffle(cut_decks)

        for cut_deck in cut_decks:
            numpy.random.shuffle(cut_deck)

        d_1 = list(itertools.chain(cut_decks[1], cut_decks[3]))
        numpy.random.shuffle(d_1)

        d_2 = list(itertools.chain(cut_decks[1], cut_decks[3]))
        numpy.random.shuffle(d_2)

        self.cards = list(itertools.chain(d_2, d_1))