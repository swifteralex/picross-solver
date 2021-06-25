# Picross Solver

[![Build Status](https://www.travis-ci.com/swifteralex/picross-solver.svg?branch=master)](https://www.travis-ci.com/github/swifteralex/picross-solver)

A python program that solves black and white nonogram (aka Picross, Paint by Numbers, Griddlers, Pic-a-Pix, Hanjie, and Japanese Crosswords) puzzles.

Can solve medium to large puzzles within a second or less; solves small puzzles nearly instantly.

## Installation

This program requires numpy and Python version 3.4 or higher to work correctly.

To install, simply run `pip install picross-solver`

## Usage

Once the package is installed, import the package with `from picross_solver import picross_solver`. After that, you should have access to the solve() function.

The solve() function takes in 3 arguments -- an array of arrays for the row clues/constraints, an array of arrays for the col clues/constraints, and a 2d numpy array representing the puzzle grid. In the puzzle grid, values -1, 0, and 1 represent a cell that is unknown, empty, or full, respectively. solve() will attempt to fill in the provided puzzle variable, overwriting the puzzle grid in the process. solve() will return True if a solution has been found, and the provided puzzle grid will be overwritten with a solution to the puzzle; it will return False if it couldn't find a solution.

## Example

### Using py

```
>>> from picross_solver import picross_solver
>>> import numpy as np
>>> rows = [[1, 1], [0], [3]]
>>> cols = [[1, 1], [1], [1, 1]]
>>> puzz = np.full((3, 3), -1)
>>> print(puzz)
[[-1 -1 -1]
 [-1 -1 -1]
 [-1 -1 -1]]
>>> picross_solver.solve(rows, cols, puzz)
True
>>> print(puzz)
[[1 0 1]
 [0 0 0]
 [1 1 1]]
```

## How it Works

This solver works by attempting to fill in a single line at a time, iterating over all of the lines and keeping track of which ones have been updated. If no progress has been made with the linesolver, the program makes a guess and recursively runs the solver.

More information about the line-solving algorithm can be found here: https://scc-forge.lancaster.ac.uk/open/nonogram/ls-fcomp
