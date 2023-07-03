from I_Game_Board import IGameBoard


class Board(IGameBoard):
    """Class for Tic Tac Toe Board"""

    def __init__(self):
        self.board_list = [*range(1, 10, 1)]

    def __str__(self):
        string_result = f' [{self.board_list[0]}] | [{self.board_list[1]}] | [{self.board_list[2]}]\n' \
                        f'-----------------\n'\
                        f' [{self.board_list[3]}] | [{self.board_list[4]}] | [{self.board_list[5]}]\n' \
                        f'-----------------\n' \
                        f' [{self.board_list[6]}] | [{self.board_list[7]}] | [{self.board_list[8]}]'
        return string_result

    def print_board(self):
        """Function to print to console a Tic Tac Toe board"""
        print(self)

    def update_board(self, move: int, move_char: str):
        """
        Function to update a Tic Tac Toe board during the playing game
        :param move: cell to be updated
        :param move_char: symbol to be placed in a cell
        """
        for index, value in enumerate(self.board_list):
            if move == value:
                self.board_list[index] = move_char
        self.print_board()
