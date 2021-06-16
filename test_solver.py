import picross_solver as solver


def test_inc_block():
    arr = [1, 1, -1, -1, -1]
    assert solver._inc_block(0, 2, arr)
    assert arr == [-1, 1, 1, -1, -1]
    arr = [1, 1, 0, -1, -1]
    assert solver._inc_block(0, 2, arr)
    assert arr == [-1, -1, 0, 1, 1]
    arr = [-1, 1, 1, 0, -1, 0, -1, -1]
    assert solver._inc_block(1, 2, arr)
    assert arr == [-1, -1, -1, 0, -1, 0, 1, 1]
    arr = [-1, -1, 1, 1, 1, 1, 0, 1, -1, -1, 1]
    assert solver._inc_block(2, 4, arr)
    assert arr == [-1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1]
    arr = [-1, 1, 1, -1, -1, -1, -1]
    assert solver._inc_block(1, 2, arr, end_index=4)
    assert arr == [-1, -1, 1, 1, -1, -1, -1]
    arr = [-1, 1, 1, -1, -1, -1, -1]
    assert solver._inc_block(1, 2, arr, possible_start=4)
    assert arr == [-1, -1, -1, -1, 1, 1, -1]
    arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0]
    assert solver._inc_block(0, 1, arr)
    assert arr == [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    arr = [1, 1, 1, 0, -1, -1, -1, 1, -1]
    assert solver._inc_block(0, 3, arr)
    assert arr == [-1, -1, -1, 0, -1, 1, 1, 1, -1]
    arr = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1]
    assert solver._inc_block(0, 3, arr)
    assert arr == [-1, -1, -1, 0, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1]

    arr = [-1, -1, 1, -1, -1]
    assert not solver._inc_block(2, 1, arr, possible_start=1, end_index=2)
    arr = [-1, 1, 1, 1, 0, 1, 1, 1]
    assert not solver._inc_block(0, 1, arr, end_index=4)
    arr = [-1, 1, 1, -1, -1, -1, -1]
    assert not solver._inc_block(1, 2, arr, end_index=3)
    arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert not solver._inc_block(0, 1, arr)
    arr = [-1, -1, -1, -1, -1, 1, 1, 1]
    assert not solver._inc_block(5, 3, arr)
    arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1]
    assert not solver._inc_block(0, 10, arr)
    arr = [1, 1, 1]
    assert not solver._inc_block(0, 3, arr)
    arr = [0, -1, -1, 1, 1, 1, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 1, 1, 1]
    assert not solver._inc_block(3, 3, arr, possible_start=5, end_index=16)
