import numpy as np
from scipy.signal import convolve2d

# AI-assistance disclosure:
# The parse_grid() function was produced with help from ChatGPT.
def parse_grid(text) :
    return np.array([
        [1 if c == '@' else 0 for c in line]
        for line in text.strip().split("\n")
    ])

def legal_row_counter(grid):
    kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])
    neighbour_array = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
    remove_zero = grid * neighbour_array
    count = np.sum((remove_zero > 0) & (remove_zero < 5))
    new_grid = remove_zero.copy() 
    new_grid[(new_grid < 5)] = 0
    new_grid[remove_zero > 4] = 1
    return count, new_grid

def solution_part_1(text):
    grid = parse_grid(text)

    count,grid = legal_row_counter(grid)
    
    return count

def solution_part_2(text):
    grid = parse_grid(text)
    total = 0
    count = 1

    while count != 0:
        count, grid = legal_row_counter(grid)
        total += count

    return total

def solve(text):
    print("Part 1:", solution_part_1(text))
    print("Part 2:", solution_part_2(text))

if __name__ == "__main__":
    with open("input.txt") as f:
        text = f.read()

    solve(text)
