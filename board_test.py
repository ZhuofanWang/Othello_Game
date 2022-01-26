from board import Board
from game_controller import GameController


def test_constructor():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 100, 20, my_gc, 1, 0)
    assert my_board.WIDTH == 800
    assert my_board.HEIGHT == 800
    assert my_board.CELL_WIDTH == 100
    assert my_board.EDGE == 10
    assert my_board.gc is my_gc
    assert my_board.u_color == 0
    assert my_board.c_color == 1


def test_init_disks():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 100, 20, my_gc, 1, 0)
    assert my_board.disks.matrix[3][3].color == 1
    assert my_board.disks.matrix[3][4].color == 0
    assert my_board.disks.matrix[4][3].color == 0
    assert my_board.disks.matrix[4][4].color == 1
    assert my_board.disks.total_disks == 4
    assert my_board.disks.white_count == 2
    assert my_board.disks.black_count == 2


def test_create_disk():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 100, 20, my_gc, 0, 1)
    my_board.create_disk(50, 50, 0)
    assert my_board.disks.matrix[0][0].color == 0
    assert my_board.disks.total_disks == 7
    assert my_board.disks.white_count == 3
    assert my_board.disks.black_count == 4


def test_update():
    gc = GameController(800, 800)
    bd = Board(800, 800, 100, 20, gc, 0, 1)
    for i in range(3):
        for j in range(8):
            bd.create_disk(50 + j*100, 50 + i*100, 0)
    for i in range(5, 8):
        for j in range(8):
            bd.create_disk(50 + j*100, 50 + i*100, 0)
    for j in range(4):
        bd.create_disk(50 + j*100, 50 + 3*100, 0)
    for j in range(4):
        bd.create_disk(50 + j*100, 50 + 4*100, 0)
    for j in range(6, 8):
        bd.create_disk(50 + j*100, 50 + 4*100, 0)
    for j in range(6, 8):
        bd.create_disk(50 + j*100, 50 + 5*100, 0)
    bd.update()
    assert bd.disks.black_count == 27
    assert bd.disks.white_count == 37
    assert bd.disks.is_full() is True
    assert bd.gc.white_count == 27
    assert bd.gc.game_over is True
    assert bd.gc.black_wins is True
