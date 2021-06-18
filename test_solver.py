import pytest
import picross_solver as solver

_ = -1


def test_push_left():
    # no drawing necessary
    rule = [3]
    arr = [_, _, _, _, _]
    assert solver._push_left(rule, arr) == [0]
    rule = [3, 1]
    arr = [0, _, 0, _, _, _, _, _]
    assert solver._push_left(rule, arr) == [3, 7]
    rule = [1, 1, 1, 1, 1]
    arr = [_, 1, 0, _, 0, 0, _, _, _, _, _]
    assert solver._push_left(rule, arr) == [1, 3, 6, 8, 10]
    rule = [6]
    arr = [0, 0, _, _, _, 1, _, _, _, 1, 1, _, _, _, _, 0, _]
    assert solver._push_left(rule, arr) == [5]
    rule = [4, 1, 3, 4]
    arr = [1, 1, _, _, 0, 0, _, 1, _, _, 1, _, 0, _, _, 1, 1, 1, 1, _]
    assert solver._push_left(rule, arr) == [0, 7, 9, 15]
    rule = [5]
    arr = [_, _, _, 1, _, _, _, 1, _, _, _]
    assert solver._push_left(rule, arr) == [3]
    rule = [5]
    arr = [_, _, _, _, _, 0, _, _, _, 1, _]
    assert solver._push_left(rule, arr) == [6]

    # need to draw
    rule = [1, 1]
    arr = [_, _, _, _, 1, _, 1]
    assert solver._push_left(rule, arr) == [4, 6]
    rule = [1, 1, 1]
    arr = [_, _, _, _, _, _, 1, 0, 1, _, 1]
    assert solver._push_left(rule, arr) == [6, 8, 10]
    rule = [1, 3]
    arr = [1, _, _, _, 1, _, 1]
    assert solver._push_left(rule, arr) == [0, 4]
    rule = [1, 5, 1, 1, 1]
    arr = [0, 0, 0, 0, 0, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 0, 0, 0, 0, 1, _, _, _, _, _, _, _, _, 0, 0, _, _, 1]
    assert solver._push_left(rule, arr) == [5, 7, 17, 22, 35]
    rule = [2, 3, 5]
    arr = [_, _, 0, 1, 1, _, 0, 0, _, _, 0, _, _, 1, _, _, _, 1, _, _]
    assert solver._push_left(rule, arr) == [0, 3, 13]
    rule = [1, 3, 2, 1]
    arr = [_, _, _, _, 1, _, 1, 1, 1, _, 1,  1, _, _, 1]
    assert solver._push_left(rule, arr) == [4, 6, 10, 14]
    rule = [5, 8]
    arr = [_, 1, 1, 1, 1, 1, 0, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1]
    assert solver._push_left(rule, arr) == [1, 10]
    rule = [1, 4, 2, 3, 2, 1, 1]
    arr = [_, 1, _, _, _, _, _, 0, 1, 1, 1, _, 0, _, _, _, _, 1, _, 1, _, _, 1, 1, _, 0, _, _, _, 1]
    assert solver._push_left(rule, arr) == [1, 8, 13, 17, 22, 26, 29]
    rule = [5, 1, 1, 1, 1, 1, 1]
    arr = [_, _, _, _, _, _, _, _, _, _, _, _, 0, 1, _, _, 1, 1, 0, _, _, _, _, _, _, _, _, _, _, _]
    assert solver._push_left(rule, arr) == [13, 19, 21, 23, 25, 27, 29]
    rule = [1, 1, 1, 5, 1, 1, 1, 1, 1, 1]
    arr = [1, _, _, _, _, 1, _, _, _, _, _, _, 0, 1, _, _, 1, 1, 0, _, _, _, _, _, _, _, _, _, _, _]
    assert solver._push_left(rule, arr) == [0, 2, 5, 13, 19, 21, 23, 25, 27, 29]
    rule = [3, 3, 2, 2, 2, 6]
    arr = [_, _, _, _, 1, _, _, _, 1, 1, 1, _, 0, 1, _, _, 1, 1, 0, _, _, 1, 1, _, 1, 1, _, _, _, _]
    assert solver._push_left(rule, arr) == [2, 8, 13, 16, 21, 24]
    rule = [2, 2, 1, 1]
    arr = [_, _, 1, _, 1, _, _, _, _, _, _, _, _, _, 1]
    assert solver._push_left(rule, arr) == [1, 4, 7, 14]


def test_push_solve():
    rule = [1]
    arr = [_]
    assert solver._push_solve(rule, arr) == [0]
    assert arr == [1]
    rule = [7]
    arr = [_, _, _, _, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [2, 3, 4, 5, 6]
    assert arr == [_, _, 1, 1, 1, 1, 1, _, _]
    rule = [7, 5]
    arr = [_, _, _, _, _, _, _, _, _, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [1, 2, 3, 4, 5, 6, 9, 10, 11, 12]
    assert arr == [_, 1, 1, 1, 1, 1, 1, _, _, 1, 1, 1, 1, _]
    rule = [2, 5]
    arr = [_, _, 1, _, _, _, _, 1, _, _, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [0, 8, 12, 13, 14]
    assert arr == [0, _, 1, _, _, _, _, 1, 1, _, _, _, 0, 0, 0]
    rule = [1, 1, 1, 4, 1, 1]
    arr = [_, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 1, _, _, 0, _, _, _]
    assert solver._push_solve(rule, arr) == [15, 16, 18, 19, 20]
    assert arr == [_, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 1, 1, 1, 0, 1, 0, 1]
    rule = [3, 5, 3]
    arr = [1, 1, 1, _, 1, 1, 1, 1, 1, _, _, _, _, _, 1]
    assert solver._push_solve(rule, arr) == [3, 9, 10, 11, 12, 13]
    assert arr == [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    rule = [1, 1, 1, 1, 1, 1]
    arr = [_, _, 1, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, 1, _, 1, _, _]
    assert solver._push_solve(rule, arr) == [0, 1, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 17, 19, 20]
    assert arr == [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
    rule = [1, 1, 1, 1, 1, 1, 1]
    arr = [_, _, 1, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, 1, _, 1, _, _]
    assert solver._push_solve(rule, arr) == []
    assert arr == [_, _, 1, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, 1, _, 1, _, _]
    rule = [1, 5, 1, 3, 7]
    arr = [_, _, _, _, _, 1, _, _, 1, 1, 1, _, 0, 1, 0, _, 1, 1, _, _, _, _, _, _, 1, _, _, _, _]
    assert solver._push_solve(rule, arr) == [0, 1, 2, 3, 4, 6, 7, 11, 22, 23, 25]
    assert arr == [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, _, 1, 1, _, _, _, _, 1, 1, 1, 1, _, _, _]

    # test error checking
    rule = [5]
    arr = [_, _, 0, _, 0, _, _, _, 0, _, _, _, 0, _, _]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)
    rule = [1, 3, 3]
    arr = [_, 1, _, 1, 1, 1, _, 0, 1, 1, 0, _]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)
    rule = [1, 3, 3]
    arr = [_, 1, _, 1, 1, 1, _, 0, 1, 1, 0, _]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)
    rule = [1, 3, 4, 3, 6, 5]
    arr = [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 1, 0, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)
    rule = [1, 1, 2]
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)
    rule = [1, 1, 2]
    arr = [1, _, 1, 1, _, _, _, _, _, _, _]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)
    rule = [1, 1, 3]
    arr = [_, _, _, _, _, _, _, _, 0, 1, _]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)
    rule = [2, 1]
    arr = [1, _, 1, _, _, _, _, _]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)
    rule = [4]
    arr = [_, _, 1, _, _, _, 1, _]
    with pytest.raises(Exception):
        x = solver._push_solve(rule, arr)


def test_solve():
    row_constraints = [[1, 1],
                       [1],
                       [1, 1]]
    col_constraints = [[1, 1],
                       [1],
                       [1, 1]]
    puzzle = [[_, _, _],
              [_, _, _],
              [_, _, _]]
    solver.solve(row_constraints, col_constraints, puzzle)
    assert puzzle == [[1, 0, 1],
                      [0, 1, 0],
                      [1, 0, 1]]

    row_constraints = [[2],
                       [1, 2],
                       [2],
                       [2],
                       [1, 1]]
    col_constraints = [[2, 1],
                       [2],
                       [1],
                       [2],
                       [2, 1]]
    puzzle = [[_, _, _, _, _],
              [_, _, _, _, _],
              [_, _, _, _, _],
              [_, _, _, _, _],
              [_, _, _, _, _]]
    solver.solve(row_constraints, col_constraints, puzzle)
    assert puzzle == [[0, 0, 0, 1, 1],
                      [1, 0, 0, 1, 1],
                      [1, 1, 0, 0, 0],
                      [0, 1, 1, 0, 0],
                      [1, 0, 0, 0, 1]]

    row_constraints = [[1, 1],
                       [3, 3],
                       [3, 3],
                       [1, 1],
                       [3, 4],
                       [3, 4],
                       [1, 1],
                       [10],
                       [9],
                       [7]]
    col_constraints = [[1],
                       [2, 2],
                       [2, 2, 3],
                       [10],
                       [2, 3],
                       [2, 3],
                       [2, 2, 3],
                       [10],
                       [2, 2, 3],
                       [2]]
    puzzle = [[_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _],
              [_, _, _, _, _, _, _, _, _, _]]
    solver.solve(row_constraints, col_constraints, puzzle)
    assert puzzle == [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                      [0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                      [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                      [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [0, 0, 1, 1, 1, 1, 1, 1, 1, 0]]
