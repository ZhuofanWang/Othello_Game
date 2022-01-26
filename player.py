from random import randint
from board import Board


class Player:
    '''A player, click on the screen to create a disk'''
    def __init__(self, board):
        self.board = board

    def player_move(self, x, y, color):
        '''player creates a disk'''
        self.board.create_disk(x, y, color)

    def computer_move(self, row, col, color):
        '''computer creates a disk'''
        self.board.create_disk(col * self.board.CELL_WIDTH +
                               self.board.CELL_WIDTH/2,
                               row * self.board.CELL_WIDTH +
                               self.board.CELL_WIDTH/2, color)
