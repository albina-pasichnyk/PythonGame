from abc import ABC, abstractmethod


class IGameBoard(ABC):
    """Abstract Class of game boards"""

    @abstractmethod
    def print_board(self): ...
