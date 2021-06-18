import numpy as np
from collections.abc import Iterable


def _push_left(rule, arr):
    block = 0
    pos = [0] * len(rule)
    solid = [-1] * len(rule)
    target = 0

    def invalid():
        nonlocal target
        nonlocal block
        solid[block] = -1
        for i in range(0, rule[block]):
            if arr[pos[block] + i] == 0:
                if solid[block] != -1:
                    target = block
                    drawing()
                    return
                pos[block] += i + 1
                invalid()
                return
            if solid[block] == -1 and arr[pos[block] + i] == 1:
                solid[block] = i

        if solid[block] == -1 and pos[block] + rule[block] < len(arr) and arr[pos[block] + rule[block]] == 1:
            solid[block] = rule[block]
        while pos[block] + rule[block] < len(arr) and arr[pos[block] + rule[block]] == 1:
            if solid[block] == 0:
                target = block
                drawing()
                return
            pos[block] += 1
            solid[block] -= 1

        if block != len(rule) - 1:
            pos[block + 1] = pos[block] + rule[block] + 1
            block += 1
            invalid()
            return
        trailing_solid_pos = -1
        for i in range(pos[block] + rule[block] + 1, len(arr)):
            if arr[i] == 1:
                trailing_solid_pos = i
                break
        if trailing_solid_pos != -1:
            if solid[block] > 0:
                pos[block] += 1
                solid[block] -= 1
                invalid()
            elif solid[block] == 0:
                target = block
                drawing()
            else:
                pos[block] = trailing_solid_pos - rule[block] + 1
                invalid()

    def drawing():
        nonlocal target
        nonlocal block
        block -= 1
        if solid[block] > 0:
            pos[block] += 1
            solid[block] -= 1
            invalid()
        elif solid[block] == 0:
            target = block
            drawing()
        else:
            pos[block] = pos[target] + solid[target] - rule[block] + 1
            invalid()

    invalid()
    return pos


def _push_solve(rule, arr):
    left_pushed_blocks = _push_left(rule, arr)
    rule.reverse()
    arr.reverse()
    right_pushed_blocks = _push_left(rule, arr)
    arr.reverse()

    temp_arr = [0] * len(arr)
    num = 0
    for block in range(0, len(rule)):
        gap_start = 0 if block == 0 else left_pushed_blocks[block - 1] + rule[len(rule) - block]
        block_size = rule[len(rule) - block - 1]
        block_pos = left_pushed_blocks[block]
        gap_end = block_pos - 1
        for j in range(gap_start, gap_end + 1):
            temp_arr[j] = num
        num += 1
        for j in range(block_pos, block_pos + block_size):
            temp_arr[j] = num
        num += 1
    capped_gap_start = left_pushed_blocks[len(rule) - 1] + rule[0]
    for i in range(capped_gap_start, len(arr)):
        temp_arr[i] = num
    num = 0
    for block in range(0, len(rule)):
        gap_start = 0 if block == 0 else len(arr) - right_pushed_blocks[len(rule) - block]
        block_size = rule[len(rule) - block - 1]
        block_pos = len(arr) - right_pushed_blocks[len(rule) - block - 1] - block_size
        gap_end = block_pos - 1
        for j in range(gap_start, gap_end + 1):
            if temp_arr[j] == num:
                arr[j] = 0
        num += 1
        for j in range(block_pos, block_pos + block_size):
            if temp_arr[j] == num:
                arr[j] = 1
        num += 1
    capped_gap_start = len(arr) - right_pushed_blocks[0]
    for i in range(capped_gap_start, len(arr)):
        if temp_arr[i] == num:
            arr[i] = 0


def solve(row_constraints, col_constraints, puzzle):
    """
    Overwrites the given puzzle variable with a solution to the nonogram.

    Parameters
    ----------
    row_constraints : Iterable[Iterable[int]]
        Defines all of the constraints in each row of the puzzle.
    col_constraints : Iterable[Iterable[int]]
        Defines all of the constraints in each column of the puzzle.
    puzzle : Iterable[Iterable[int]]
        Overwritten with the nonogram solution. Should only contain values -1
         (unknown), 0 (empty), or 1 (filled).

    Returns
    -------
    is_solved : boolean
        Returns a boolean representing if the function was able to solve the
         nonogram or not. True means it was able to be solved with no issues;
         False means the puzzle was unable to be solved.

    Examples
    --------
    >>> puz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    >>> rows = [[1, 1], [0], [3]]
    >>> cols = [[1, 1], [1], [1, 1]]
    >>> solve(rows, cols, puz)
    Variable 'puz' will now be [[1, 0, 1], [0, 0, 0], [1, 1, 1]]

    >>> puz = np.full((2, 3), -1)
    >>> rows = [[3], [1]]
    >>> cols = [[1], [2], [1]]
    >>> solve(rows, cols, puz)
    Variable 'puz' will now be [[1, 1, 1], [0, 1, 0]]

    >>> puz = np.full((2, 2), 0)
    >>> rows = [[2], [2]]
    >>> cols = [[2], [2]]
    >>> solve(rows, cols, puz)
    Puzzle can't be resolved; returns False

    """
    return 0
