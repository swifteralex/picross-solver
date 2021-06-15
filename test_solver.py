import picross_solver as solver


def test_fill_row():
    row_constraint = [1, 1, 1]
    row = [-1, -1, -1, -1, -1]
    solver._fill_row(row_constraint, row)
    assert row == [1, 0, 1, 0, 1]
