import numpy as np
from collections.abc import Iterable


def _fill_row(row_constraint, row):
    return 0


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
    exit_code : boolean
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
