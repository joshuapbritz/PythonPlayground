# GLOBALS
GAME_HAS_WINNER = False
CURRENT_PLAYER = 1
PLAYER_CHAR_MAP = {
    1: {
        'char': 'X',
        'moves': []
    },
    2: {
        'char': '0',
        'moves': []
    }
}
GAME_IN_PROGRESS = False
AVAILABLE_MOVES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
WINNING_MOVES = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8),
                 (3, 6, 9), (1, 5, 9), (3, 5, 7))
BOARD = '     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  \n_____|_____|_____\n     |     |     \n  7  |  8  |  9  \n     |     |     \n'


def set_player(k):
    global CURRENT_PLAYER
    CURRENT_PLAYER = k


def reconfigure_game():
    global GAME_IN_PROGRESS
    global GAME_HAS_WINNER
    global AVAILABLE_MOVES
    global PLAYER_CHAR_MAP
    global BOARD
    global CURRENT_PLAYER

    GAME_IN_PROGRESS = False
    GAME_HAS_WINNER = False
    AVAILABLE_MOVES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    PLAYER_CHAR_MAP = {
        1: {
            'char': 'X',
            'moves': []
        },
        2: {
            'char': '0',
            'moves': []
        }
    }
    BOARD = '     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  \n_____|_____|_____\n     |     |     \n  7  |  8  |  9  \n     |     |     \n'
    CURRENT_PLAYER = 1
    start_game()


def check_winner():
    # Check for winner
    has_won = False
    m_moves = PLAYER_CHAR_MAP[CURRENT_PLAYER]['moves']

    for winning_move in WINNING_MOVES:
        v = list(winning_move)
        for move_value in winning_move:
            if move_value in m_moves:
                v.remove(move_value)
        has_won = len(v) == 0
        if has_won: break

    return has_won


def print_board(value=None):
    global BOARD
    if value != None:
        BOARD = BOARD.replace(
            str(value), PLAYER_CHAR_MAP[CURRENT_PLAYER]['char'])

    print(BOARD)


def start_game():
    global GAME_IN_PROGRESS
    global GAME_HAS_WINNER
    print_board()
    result = input('Are you ready to play? [Y/n]: ')
    if result == '' or result.lower() == 'y':
        print('starting')
        GAME_IN_PROGRESS = True
        while GAME_IN_PROGRESS:
            if len(AVAILABLE_MOVES) == 0:
                break
            p_char = PLAYER_CHAR_MAP[CURRENT_PLAYER]['char']
            print('Available Moves: ' +
                  ', '.join(list(map(lambda v: str(v), AVAILABLE_MOVES))))

            player_move = int(
                input('Your turn player {0} ({1}): '.format(
                    CURRENT_PLAYER, p_char)))

            if player_move in AVAILABLE_MOVES:
                print_board(player_move)
                AVAILABLE_MOVES.remove(player_move)
                PLAYER_CHAR_MAP[CURRENT_PLAYER]['moves'].append(player_move)

                player_has_won = check_winner()
                GAME_HAS_WINNER = True

                if not player_has_won:
                    if CURRENT_PLAYER == 1:
                        set_player(2)
                    else:
                        set_player(1)
                else:
                    GAME_HAS_WINNER = True
                    break
            else:
                print('\nThat move is not available, try again\n')

        if GAME_HAS_WINNER:
            print('Game Over. Player ' + str(CURRENT_PLAYER) + ' wins')
        else:
            print('It\'s a draw')

        play_again = input('would you like to play again? [Y/n]: ')

        if play_again == '' or play_again.lower() == 'y':
            reconfigure_game()
        else:
            print('Thank you for playing :)')


start_game()
