

def print_grid(grid):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end=" ")
        print()


#Check the validity of the number insert function
def is_valid(grid, row, col, num, size):

    #Check if number exists in row
    for x in range(9):
        if grid[row][x] == num:
            return False
        
    #Check if number exists in col
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    #check Sub-grid
    box_size = int(size ** 0.5)
    corner_row = row - row % box_size
    corner_col = col - col % box_size
    for x in range(box_size):
        for y in range(box_size):
            if grid[corner_row + x][corner_col + y] == num:
                return False
    
    return True


# Recursively solves for the puzzel function
def solve_puzzle(grid, row, col, size):

    #Handels overflow to not go out of bounds of the grid
    if col == size:
        if row == size - 1:
            return True
        row += 1
        col = 0

    #Skips any cells that are pre-filled
    if grid[row][col] > 0:
        return solve_puzzle(grid, row, col + 1, size)
    
    #Loops through trying numbers 1 - 9 | Checks is the move valid | Will reset to 0 if does not work until all options are exhausted
    for num in range(1, size + 1):
        if is_valid(grid, row, col, num, size):
            grid[row][col] = num

            if solve_puzzle(grid, row, col + 1, size):
                return True
        
        grid[row][col] = 0
    
    return False


def solve_puzzle_call(grid):
    size = len(grid)
    if solve_puzzle(grid, 0, 0, size):
        print_grid(grid)
        print()
    
    else:
        print("No solution available")


#Initialize user input for grid size then solves/formats response
def main():
    print("Choose the size of the Sudoku puzzle:")
    print("1. 2x2")
    print("2. 3x3")
    print("3. 4x4")
    print("4. 5x5")
    
    choice = int(input("Enter your choice (1-4): "))
    
    sizes = [2, 3, 4, 5]
    if choice in [1, 2, 3, 4]:
        size = sizes[choice - 1]
        solve_puzzle_call(grid)
    else:
        print("Invalid choice. Please select a number between 1 and 4.")




grid = [
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


#Call the solving function
main()