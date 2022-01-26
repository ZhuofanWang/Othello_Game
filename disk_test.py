from disk import Disk


def test_constructor():
    d = Disk(0, 0, 1, 200, 20)
    assert d.row == 0
    assert d.col == 0
    assert d.color == 1
    assert d.CELL_WIDTH == 200
    assert d.EDGE == 20


def test___repr__():
    d = Disk(0, 0, 1, 200, 20)
    assert print(d) == print("1")
