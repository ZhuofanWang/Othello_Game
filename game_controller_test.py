from game_controller import GameController


def test_constructor():
    gc = GameController(800, 800)
    assert gc.WIDTH == 800
    assert gc.HEIGHT == 800
    assert gc.game_over is False
    assert gc.black_wins is False
    assert gc.white_wins is False
    assert gc.a_tie is False
    assert gc.black_count == 0
    assert gc.white_count == 0
    assert gc.computer_loading is False
    assert gc.waiting == 0
