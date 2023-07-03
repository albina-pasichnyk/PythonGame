from Play_Game_Round import PlayGameRound


class TicTacToe:
    """Class of Tic Tac Toe game"""

    @staticmethod
    def play():
        """Method to start playing a Tic Tac Toe game"""
        game_round = PlayGameRound()
        game_round.play_round()


if __name__ == '__main__':
    TicTacToe.play()
