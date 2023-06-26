import sys

from Tic_Tac_Toe_Board_Class import Board


class PlayGameRound:
    """Class to play and process round of Tic Tac Toe game"""

    def __init__(self):
        self.board = None

    def start_game_decorator(function):
        def wrapper(*args):
            header, footer = '*' * 23, '*' * 23
            return f'{header}\n{function(*args)}\n{footer}'

        return wrapper

    @start_game_decorator
    def show_game_intro(self):
        return f'Let\'s play Tic-Tac-Toe!\n' \
               f'\n' \
               f'Initially provide one by one names of players.\n' \
               f'When game board is shown, player has to type number of sell which he/she wants to use as a move.\n' \
               f'Respective mark will be added.\n' \
               f'The first player to get 3 of his/her marks in a row (up, down or diagonally) is the winner\n' \
               f'\n' \
               f'If you want to quit the game type "exit"\n '

    def __get_player_name(self):
        """Function to get player's name"""
        self.player_1 = input('Please enter name of 1st player\n')
        self.player_2 = input('Please enter name of 2nd player\n')

    def __next_move(self, player_name: str, move_char: str):
        """
        Function to process and proceed with next player's move
        :param player_name: player's name who's turn to take a move
        :param move_char: player's symbol to place in a cell
        """
        while True:
            input_move = input(f'{player_name} Move: Please enter a position number:\n')
            if input_move == 'exit':
                sys.exit()
            if not input_move.isdecimal():
                print('Only numbers are allowed')
                continue
            input_move = int(input_move)
            if input_move not in range(1, 10):
                print('Non-existing move')
                continue
            break
        print(f'{player_name} entered {input_move}')
        self.board.update_board(input_move, move_char)

    def __check_win(self):
        """Function to check if there is a winner in a game round"""
        if self.board.board_list[0] == self.board.board_list[1] == self.board.board_list[2]:
            return True
        if self.board.board_list[3] == self.board.board_list[4] == self.board.board_list[5]:
            return True
        if self.board.board_list[6] == self.board.board_list[7] == self.board.board_list[8]:
            return True
        if self.board.board_list[0] == self.board.board_list[3] == self.board.board_list[6]:
            return True
        if self.board.board_list[1] == self.board.board_list[4] == self.board.board_list[7]:
            return True
        if self.board.board_list[2] == self.board.board_list[5] == self.board.board_list[8]:
            return True
        if self.board.board_list[0] == self.board.board_list[4] == self.board.board_list[8]:
            return True
        if self.board.board_list[6] == self.board.board_list[4] == self.board.board_list[2]:
            return True
        else:
            return False

    def processing_round(self):
        """Function to process the round of Tic Tac Toe game"""
        move_counter = 1
        while not self.__check_win():
            current_user = ''
            if move_counter % 2 != 0:
                current_user = self.player_1
                self.__next_move(f'{current_user}\'s', 'X')
            else:
                current_user = self.player_2
                self.__next_move(f'{current_user}\'s', 'O')
            move_counter += 1
            if self.__check_win() is True:
                print(f'\nCongratulations! {current_user} wins the game')
                break
            if move_counter == 10:
                print('Game is over! No one wins.')
                break

    def play_round(self):
        """Function to play a round of Tic Tac Toe game"""
        print(self.show_game_intro())
        self.board = Board()
        self.__get_player_name()
        self.board.print_board()
        self.processing_round()
