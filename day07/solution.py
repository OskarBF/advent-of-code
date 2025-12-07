import numpy as np

# AI-assistance disclosure:
# The parse_grid() and find_split() functions were produced with help from ChatGPT.

def parse_grid(text):
    """
    Converts the input text into a numpy array of characters.
    """
    return np.array(
        [list(row) for row in text.strip().split("\n")],
        dtype="U1"
    )


def find_split(grid, i, start):
    """
    Fires the laser downward starting at column i and row start.
    When hitting '^', the laser splits left and right and continues.
    Returns the total number of '^' hit in this path.
    """
    j = i + 1     # right
    k = i - 1     # left
    nrows, ncols = grid.shape

    for dist in range(start, nrows):
        cell = grid[dist, i]

        if cell == '|':
            return 0

        elif cell == '^':
            left = find_split(grid, j, dist) if j < ncols else 0
            right = find_split(grid, k, dist) if k >= 0 else 0
            return 1 + left + right

        else:
            grid[dist, i] = '|'

    return 0


def shooting_lazer(grid):
    """
    Finds the 'S' in the top row and fires the laser downward.
    Returns the number of '^' hit.
    """
    i = 0
    while grid[0, i] != "S":
        i += 1

    return find_split(grid, i, 1)


def solution(text):
    grid = parse_grid(text)
    return shooting_lazer(grid)


def solve(text):
    print("Part 1:", solution(text))


if __name__ == "__main__":
    with open("input.txt") as f:
        text = f.read()

    solve(text)
