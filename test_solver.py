import pytest
import numpy as np
import picross_solver as solver

_ = -1


def test_push_solve():
    rule = [1]
    arr = [_]
    assert solver._push_solve(rule, arr) == [0]
    assert np.all(arr == np.array(
        [1]))
    rule = [7]
    arr = [_, _, _, _, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [2, 3, 4, 5, 6]
    assert np.all(arr == np.array(
        [_, _, 1, 1, 1, 1, 1, _, _]))
    rule = [7, 5]
    arr = [_, _, _, _, _, _, _, _, _, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [1, 2, 3, 4, 5, 6, 9, 10, 11, 12]
    assert np.all(arr == np.array(
        [_, 1, 1, 1, 1, 1, 1, _, _, 1, 1, 1, 1, _]))
    rule = [2, 5]
    arr = [_, _, 1, _, _, _, _, 1, _, _, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [0, 8, 12, 13, 14]
    assert np.all(arr == np.array(
        [0, _, 1, _, _, _, _, 1, 1, _, _, _, 0, 0, 0]))
    rule = [1, 1, 1, 4, 1, 1]
    arr = [_, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 1, _, _, 0, _, _, _]
    assert solver._push_solve(rule, arr) == [15, 16, 18, 19, 20]
    assert np.all(arr == np.array(
        [_, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 1, 1, 1, 0, 1, 0, 1]))
    rule = [3, 5, 3]
    arr = [1, 1, 1, _, 1, 1, 1, 1, 1, _, _, _, _, _, 1]
    assert solver._push_solve(rule, arr) == [3, 9, 10, 11, 12, 13]
    assert np.all(arr == np.array(
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]))
    rule = [1, 1, 1, 1, 1, 1]
    arr = [_, _, 1, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, 1, _, 1, _, _]
    assert solver._push_solve(rule, arr) == [0, 1, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 17, 19, 20]
    assert np.all(arr == np.array(
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]))
    rule = [1, 1, 1, 1, 1, 1, 1]
    arr = [_, _, 1, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, 1, _, 1, _, _]
    assert solver._push_solve(rule, arr) == [1, 3, 6, 8, 10, 12, 14, 15, 17, 19]
    assert np.all(arr == np.array(
        [_, 0, 1, 0, _, _, 0, 1, 0, _, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, _]))
    rule = [1, 5, 1, 3, 7]
    arr = [_, _, _, _, _, 1, _, _, 1, 1, 1, _, 0, 1, 0, _, 1, 1, _, _, _, _, _, _, 1, _, _, _, _]
    assert solver._push_solve(rule, arr) == [0, 1, 2, 3, 4, 6, 7, 11, 22, 23, 25]
    assert np.all(arr == np.array(
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, _, 1, 1, _, _, _, _, 1, 1, 1, 1, _, _, _]))
    rule = [1, 5, 1, 1, 1]
    arr = [0, 0, 0, 0, 0, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 0, 0, 0, 0, 1, _, _, _, _, _, _, _, _, 0, 0, _, _, 1]
    assert solver._push_solve(rule, arr) == [27, 34]
    assert np.all(arr == np.array(
        [0, 0, 0, 0, 0, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 0, 0, 0, 0, 1, _, _, _, _, 0, _, _, _, 0, 0, _, 0, 1]))
    rule = [0]
    arr = [_, _, _, _, _]
    assert solver._push_solve(rule, arr) == [0, 1, 2, 3, 4]
    assert np.all(arr == np.array(
        [0, 0, 0, 0, 0]))
    rule = [0]
    arr = [_, 0, 0, _, _]
    assert solver._push_solve(rule, arr) == [0, 3, 4]
    assert np.all(arr == np.array(
        [0, 0, 0, 0, 0]))
    rule = []
    arr = [0, 0, 0, 0]
    assert solver._push_solve(rule, arr) == []
    assert np.all(arr == np.array(
        [0, 0, 0, 0]))
    rule = [9, 1, 1, 1]
    arr = [_, _, _, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, _, _, _, 1, 0, _, 0, _]
    assert solver._push_solve(rule, arr) == [0, 1, 2, 23]
    assert np.all(arr == np.array(
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, _, _, 0, 1, 0, _, 0, _]))
    rule = [5, 6, 3, 1, 1]
    arr = [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 0, _, 0, 0, 0, 0, 0,
           _, _, _, _, _, _, 1, 1, 0, _, _, _, _, _, _, 0, 0, 0, _, _, _, 1, 0]
    assert solver._push_solve(rule, arr) == [9, 11, 12, 13, 14, 17, 23, 24, 28, 43]
    assert np.all(arr == np.array(
        [_, _, _, _, _, _, _, _, _, 0, _, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
         0, 0, _, _, _, 1, 1, 1, 0, _, _, _, _, _, _, 0, 0, 0, _, _, 0, 1, 0]))
    rule = [2, 1, 1]
    arr = [_, _, _, 1, _, _, 0, _, 0, _, _, 1, _, _, _]
    assert solver._push_solve(rule, arr) == [10, 12]
    assert np.all(arr == np.array(
        [_, _, _, 1, _, _, 0, _, 0, _, 0, 1, 0, _, _]))

    # test error checking
    rule = [5]
    arr = [_, _, 0, _, 0, _, _, _, 0, _, _, _, 0, _, _]
    assert solver._push_solve(rule, arr) == [-1]
    rule = [1, 3, 3]
    arr = [_, 1, _, 1, 1, 1, _, 0, 1, 1, 0, _]
    assert solver._push_solve(rule, arr) == [-1]
    rule = [1, 3, 3]
    arr = [_, 1, _, 1, 1, 1, _, 0, 1, 1, 0, _]
    assert solver._push_solve(rule, arr) == [-1]
    rule = [1, 3, 4, 3, 6, 5]
    arr = [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 0, 1, 1, 0, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [-1]
    rule = [1, 1, 2]
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert solver._push_solve(rule, arr) == [-1]
    rule = [1, 1, 2]
    arr = [1, _, 1, 1, _, _, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [-1]
    rule = [1, 1, 3]
    arr = [_, _, _, _, _, _, _, _, 0, 1, _]
    assert solver._push_solve(rule, arr) == [-1]
    rule = [2, 1]
    arr = [1, _, 1, _, _, _, _, _]
    assert solver._push_solve(rule, arr) == [-1]
    rule = [4]
    arr = [_, _, 1, _, _, _, 1, _]
    assert solver._push_solve(rule, arr) == [-1]


def test_solve():
    row_constraints = [[1, 1],
                       [1],
                       [1, 1]]
    col_constraints = [[1, 1],
                       [1],
                       [1, 1]]
    puzzle = np.full((3, 3), _)
    solver.solve(row_constraints, col_constraints, puzzle)
    assert np.all(puzzle == np.array(
        [[1, 0, 1],
         [0, 1, 0],
         [1, 0, 1]]
    ))

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
    puzzle = np.full((5, 5), _)
    solver.solve(row_constraints, col_constraints, puzzle)
    assert np.all(puzzle == np.array(
        [[0, 0, 0, 1, 1],
         [1, 0, 0, 1, 1],
         [1, 1, 0, 0, 0],
         [0, 1, 1, 0, 0],
         [1, 0, 0, 0, 1]]
    ))

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
    puzzle = np.full((10, 10), _)
    solver.solve(row_constraints, col_constraints, puzzle)
    assert np.all(puzzle == np.array(
        [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0]]))

    row_constraints = [[1, 2],
                       [1, 2],
                       [1, 2],
                       [1, 2]]
    col_constraints = [[4],
                       [0],
                       [0],
                       [0],
                       [0],
                       [4],
                       [4]]
    puzzle = np.full((4, 7), _)
    solver.solve(row_constraints, col_constraints, puzzle)
    assert np.all(puzzle == np.array(
        [[1, 0, 0, 0, 0, 1, 1],
         [1, 0, 0, 0, 0, 1, 1],
         [1, 0, 0, 0, 0, 1, 1],
         [1, 0, 0, 0, 0, 1, 1]]))

    row_constraints = [[2, 2],
                       [1, 1, 2, 1],
                       [1, 2, 2, 2],
                       [2, 1, 2, 2],
                       [1, 6, 2],
                       [2, 5, 1, 1],
                       [1, 9, 1],
                       [2, 4, 2, 1],
                       [4, 2, 1],
                       [1, 1, 1, 1, 2],
                       [2, 1, 1],
                       [1, 7, 1],
                       [1, 7],
                       [1, 1, 1, 4],
                       [1, 1, 1, 1, 2]]
    col_constraints = [[3],
                       [1, 3],
                       [1, 1, 3],
                       [3, 1, 6],
                       [3, 1, 1],
                       [5, 1, 2],
                       [7, 1],
                       [6, 4],
                       [1, 4, 2],
                       [1, 1, 1, 1, 4],
                       [1, 1, 1, 1, 3],
                       [1, 1, 9],
                       [1, 1, 4, 3],
                       [1, 1, 1, 4],
                       [1, 5]]
    puzzle = np.full((15, 15), _)
    solver.solve(row_constraints, col_constraints, puzzle)
    assert np.all(puzzle == np.array(
        [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
         [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
         [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
         [0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
         [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0]]))

    row_constraints = [[4, 4, 1, 1, 4, 5],
                       [3, 4, 1, 10, 1, 4, 4],
                       [3, 3, 16, 3, 4],
                       [2, 3, 18, 3, 3],
                       [2, 2, 20, 3, 3],
                       [2, 2, 22, 2, 3],
                       [2, 1, 2, 12, 2, 2, 3],
                       [1, 2, 2, 8, 2, 2, 2],
                       [3, 1, 4, 6, 4, 1, 3, 1],
                       [2, 1, 2, 2, 2, 1, 2],
                       [1, 1, 2, 2, 1, 2],
                       [1, 1, 4, 4, 1, 2],
                       [7, 7, 1],
                       [1, 1, 2, 1, 2, 1],
                       [1, 4, 4, 1],
                       [2, 1, 2, 1, 2, 1, 1],
                       [2, 1, 2, 2, 1, 1],
                       [2, 1, 1, 1, 1, 1],
                       [2, 1, 3, 3, 1, 2],
                       [2, 2, 2, 3],
                       [2, 2, 2, 3],
                       [3, 2, 1, 1, 2, 3],
                       [3, 2, 2, 4],
                       [4, 2, 1, 1, 2, 5],
                       [4, 2, 1, 2, 1, 2, 5],
                       [5, 2, 2, 4, 2, 2, 6],
                       [5, 2, 4, 4, 2, 6],
                       [6, 2, 2, 2, 2, 6],
                       [5, 3, 3, 5],
                       [5, 1, 2, 2, 1, 5],
                       [4, 1, 2, 2, 1, 5],
                       [4, 1, 3, 3, 1, 4],
                       [2, 1, 14, 1, 4],
                       [2, 18, 2],
                       [18]]
    col_constraints = [[8, 3],
                       [7, 2, 13],
                       [3, 2, 17],
                       [1, 9, 11],
                       [5, 6, 11],
                       [4, 2, 4, 9],
                       [3, 3, 1, 1, 4, 5],
                       [2, 3, 1, 1, 1, 4],
                       [1, 3, 1, 5, 10],
                       [4, 1, 3, 3, 1, 2, 2],
                       [6, 1, 5, 1, 1, 2, 3],
                       [5, 1, 5, 1, 3, 6],
                       [6, 1, 2, 5],
                       [7, 2, 4],
                       [8, 1, 2, 3],
                       [8, 2, 3],
                       [9, 2, 3],
                       [9, 2, 3],
                       [8, 2, 3],
                       [8, 1, 2, 3],
                       [7, 2, 4],
                       [6, 1, 2, 5],
                       [5, 1, 5, 1, 3, 6],
                       [6, 1, 3, 3, 1, 2, 3],
                       [4, 1, 5, 1, 1, 2, 2],
                       [1, 3, 1, 5, 10],
                       [2, 3, 1, 1, 1, 4],
                       [3, 3, 1, 1, 4],
                       [5, 2, 4, 8],
                       [6, 6, 11],
                       [1, 9, 12],
                       [3, 2, 14],
                       [7, 2, 15],
                       [8, 3, 10],
                       [9, 5]]
    puzzle = np.full((35, 35), _)
    solver.solve(row_constraints, col_constraints, puzzle)
    assert np.all(puzzle == np.array(
        [[1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
         [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
         [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
         [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
         [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
         [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
         [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

    row_constraints = [[15, 2, 1, 2],
                       [8, 3, 2, 2, 2],
                       [4, 3, 1, 2, 1, 2],
                       [6, 2, 3, 3, 2, 2, 1],
                       [4, 2, 1, 1, 3, 2, 3],
                       [3, 1, 2, 2, 2, 2, 2, 2],
                       [3, 1, 1, 3, 2, 2, 3],
                       [5, 2, 2, 1, 2, 3, 2, 3],
                       [2, 1, 2, 3, 2, 1, 2, 2, 3, 3],
                       [2, 2, 2, 2, 3, 1, 2, 2, 3, 3],
                       [2, 2, 2, 2, 3, 1, 2, 2, 3, 3],
                       [1, 2, 2, 1, 2, 1, 1, 2, 3, 3],
                       [2, 3, 1, 1, 4, 3, 3],
                       [4, 3, 1, 3, 1, 3, 1],
                       [2, 7, 1, 1, 1],
                       [6, 1, 1],
                       [1, 1, 1],
                       [1, 2, 6, 4, 1],
                       [2, 2, 6, 8, 2],
                       [2, 1, 3, 6, 9, 2],
                       [2, 1, 2, 6, 10, 2],
                       [4, 7, 10, 1],
                       [13, 6, 3, 2],
                       [14, 5, 2, 2, 2],
                       [1, 4, 9, 5, 5, 1],
                       [2, 12, 6, 5, 1, 2],
                       [9, 2, 2, 4, 5, 1, 2],
                       [5, 5, 4, 2, 5, 2, 2],
                       [4, 5, 8, 1, 5, 2, 2],
                       [1, 3, 4, 4, 1, 5, 2],
                       [2, 1, 2, 4, 3, 3],
                       [4, 3, 3, 4],
                       [4, 3, 3, 5, 1],
                       [4, 5, 4, 6],
                       [1, 3, 1, 1, 1, 1, 3, 1, 3]]
    col_constraints = [[2, 2],
                       [3, 2, 1, 2, 2],
                       [4, 2, 3, 2, 1, 3],
                       [5, 2, 4, 2, 1, 3],
                       [6, 1, 3, 1, 2, 6, 1],
                       [2, 3, 4, 8, 2],
                       [6, 1, 2, 1, 6, 2],
                       [4, 2, 2, 4, 5],
                       [1, 1, 2, 2, 8, 1],
                       [2, 2, 1, 2, 7, 2],
                       [2, 2, 1, 1, 2, 7, 5],
                       [2, 2, 1, 2, 7, 1, 4],
                       [1, 1, 1, 9, 2, 4],
                       [1, 1, 3, 2, 1, 10, 4],
                       [1, 1, 6, 1, 1, 10, 3],
                       [1, 3, 3, 8, 2],
                       [1, 2, 3, 1, 7, 5, 2],
                       [1, 1, 6, 1, 5, 9],
                       [1, 5, 1, 1, 2, 8],
                       [1, 1, 6, 9, 6],
                       [1, 6, 1, 11, 2],
                       [2, 2, 13],
                       [6, 1, 10, 1],
                       [1, 7, 2, 7, 3, 1],
                       [1, 4, 1, 5, 11],
                       [1, 2, 6, 4, 12],
                       [1, 2, 9, 3, 12],
                       [1, 1, 4, 4, 6],
                       [1, 2, 6, 7, 3, 1],
                       [1, 1, 10, 2, 7],
                       [1, 1, 9, 9],
                       [1, 2, 7, 4],
                       [2, 10, 6, 3],
                       [1, 1, 11, 7, 2],
                       [2, 7, 4, 2]]
    puzzle = np.full((35, 35), _)
    solver.solve(row_constraints, col_constraints, puzzle)
    assert np.all(puzzle == np.array(
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
         [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1],
         [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
         [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
         [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
         [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
         [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
         [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
         [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
         [0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]]))
