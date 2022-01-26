from disks import Disks


def test_constructor():
    ds = Disks(800, 800, 100, 20, 1, 0)
    assert ds.WIDTH == 800
    assert ds.HEIGHT == 800
    assert ds.CELL_WIDTH == 100
    assert ds.EDGE == 20
    assert ds.num_of_rows == int(ds.HEIGHT/ds.CELL_WIDTH)
    assert ds.num_of_cols == int(ds.WIDTH/ds.CELL_WIDTH)
    assert ds.matrix == [[None] * ds.num_of_cols
                         for i in range(ds.num_of_rows)]
    assert ds.black_count == 0
    assert ds.white_count == 0
    assert ds.total_disks == 0
    assert ds.u_color == 1
    assert ds.c_color == 0


def test_create():
    ds = Disks(800, 800, 100, 20, 1, 0)
    ds.create(50, 50, 1)
    assert ds.matrix[0][0].color == 0
    assert ds.black_count == 1
    assert ds.white_count == 0
    assert ds.total_disks == 0


def test_is_full():
    ds = Disks(800, 800, 100, 20, 1, 0)
    for j in range(8):
        ds.create(50+j*100, 50, 0)
    assert ds.is_full() is False
    for i in range(1, 8):
        for j in range(8):
            ds.create(50+j*100, 50+i*100, 0)
    assert ds.is_full() is True
