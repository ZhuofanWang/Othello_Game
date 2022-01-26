from board import Board
from game_controller import GameController
from player import Player
from game_manager import GameManager
import time

SIZE = 8
CELL_WIDTH = 100
WIDTH = 100 * SIZE
HEIGHT = 100 * SIZE
EDGE = 20 
USER_COLOR = 0
COMPUTER_COLOR = 1
TIME_ECCLIPSE = 60

game_controller = GameController(WIDTH, HEIGHT)
board = Board(WIDTH, HEIGHT, CELL_WIDTH, EDGE, game_controller,
              USER_COLOR, COMPUTER_COLOR)
player = Player(board)
computer = Player(board)
gm = GameManager(player, computer, board, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


time_counter = 0


def draw():
    global time_counter
    background(0, 0.5, 0)
    board.display()
    if not gm.player_turn and not game_controller.game_over:
        if time_counter <= TIME_ECCLIPSE:
            game_controller.computer_loading = True
            time_counter += 1
        else:
            game_controller.computer_loading = False
            gm.computer_make_move()
            time_counter = 0
    game_controller.update()


def mousePressed():
    if gm.player_turn:
        gm.player_make_move(mouseX, mouseY)
