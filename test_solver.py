import nonogram_resolver as nr


def test_fill_row():
    row_constraint = [1, 1, 1]
    row = [-1, -1, -1, -1, -1]
    nr._fill_row(row_constraint, row)
    assert row == [1, 0, 1, 0, 1]
