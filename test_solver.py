import picross_solver as solver


def test_push_left():
    # no drawing necessary
    constraints = [3]
    arr = [-1, -1, -1, -1, -1]
    assert solver._push_left(constraints, arr) == [0]
    constraints = [3, 1]
    arr = [0, -1, 0, -1, -1, -1, -1, -1]
    assert solver._push_left(constraints, arr) == [3, 7]
    constraints = [1, 1, 1, 1, 1]
    arr = [-1, 1, 0, -1, 0, 0, -1, -1, -1, -1,
           -1]
    assert solver._push_left(constraints, arr) == [1, 3, 6, 8, 10]
    constraints = [6]
    arr = [0, 0, -1, -1, -1, 1, -1, -1, -1, 1,
           1, -1, -1, -1, -1, 0, -1]
    assert solver._push_left(constraints, arr) == [5]
    constraints = [4, 1, 3, 4]
    arr = [1, 1, -1, -1, 0, 0, -1, 1, -1, -1,
           1, -1, 0, -1, -1, 1, 1, 1, 1, -1]
    assert solver._push_left(constraints, arr) == [0, 7, 9, 15]

    # need to draw
    constraints = [1, 1]
    arr = [-1, -1, -1, -1, 1, -1, 1]
    assert solver._push_left(constraints, arr) == [4, 6]
    constraints = [1, 1, 1]
    arr = [-1, -1, -1, -1, -1, -1, 1, 0, 1, -1, 1]
    assert solver._push_left(constraints, arr) == [6, 8, 10]
    constraints = [1, 3]
    arr = [1, -1, -1, -1, 1, -1, 1]
    assert solver._push_left(constraints, arr) == [0, 4]
    constraints = [1, 5, 1, 1, 1]
    arr = [0, 0, 0, 0, 0, -1, -1, -1, -1, -1,
           -1, -1, -1, -1, -1, -1, 0, 1, 0, 0,
           0, 0, 1, -1, -1, -1, -1, -1, -1, -1,
           -1, 0, 0, -1, -1, 1]
    assert solver._push_left(constraints, arr) == [5, 7, 17, 22, 35]
    constraints = [2, 3, 5]
    arr = [-1, -1, 0, 1, 1, -1, 0, 0, -1, -1,
           0, -1, -1, 1, -1, -1, -1, 1, -1, -1]
    assert solver._push_left(constraints, arr) == [0, 3, 13]
    constraints = [1, 3, 2, 1]
    arr = [-1, -1, -1, -1, 1, -1, 1, 1, 1, -1,
           1,  1, -1, -1, 1]
    assert solver._push_left(constraints, arr) == [4, 6, 10, 14]
    constraints = [5, 8]
    arr = [-1, 1, 1, 1, 1, 1, 0, -1, -1, -1,
           1, 1, 1, 1, 1, 1, 1, 1]
    assert solver._push_left(constraints, arr) == [1, 10]
    constraints = [1, 4, 2, 3, 2, 1, 1]
    arr = [-1, 1, -1, -1, -1, -1, -1, 0, 1, 1,
           1, -1, 0, -1, -1, -1, -1, 1, -1, 1,
           -1, -1, 1, 1, -1, 0, -1, -1, -1, 1]
    assert solver._push_left(constraints, arr) == [1, 8, 13, 17, 22, 26, 29]
    constraints = [5, 1, 1, 1, 1, 1, 1]
    arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
           -1, -1, 0, 1, -1, -1, 1, 1, 0, -1,
           -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert solver._push_left(constraints, arr) == [13, 19, 21, 23, 25, 27, 29]
    constraints = [1, 1, 1, 5, 1, 1, 1, 1, 1, 1]
    arr = [1, -1, -1, -1, -1, 1, -1, -1, -1, -1,
           -1, -1, 0, 1, -1, -1, 1, 1, 0, -1,
           -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert solver._push_left(constraints, arr) == [0, 2, 5, 13, 19, 21, 23, 25, 27, 29]
    constraints = [3, 3, 2, 2, 2, 6]
    arr = [-1, -1, -1, -1, 1, -1, -1, -1, 1, 1,
           1, -1, 0, 1, -1, -1, 1, 1, 0, -1,
           -1, 1, 1, -1, 1, 1, -1, -1, -1, -1]
    assert solver._push_left(constraints, arr) == [2, 8, 13, 16, 21, 24]
