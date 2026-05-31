# if snake is in the boundaries, or in itself, game ends, and return score. if snake is in the apple, increment score
def check_status(grid, score):
    x = 0
    y = 0

    for x in range(0, 10):
        for y in range(0, 10):
            value = grid[x][y]

            # snake is in boundaries
            if "#" in value and "%" in value:
                return False
            
            # snake is in itself
            if "%" in value:
                occurances = 0
                for object in value:
                    if object == "%":
                        occurances += 1

                if occurances > 1:
                    return False       
                 

# get player input and translate the snake

# create a blank grid (an array with strings that make up each row) with the snake, and the apple

# add apple in a random spot in the grid that isnt the snake, or the player wins

# put snake in a random spot

# define an empty grid, and set up game loop
def play_game ():
    grid = []

    # add arrays inside grid

    for x in range(0, 10):
        grid.append([])

    ended = False

    # set up grid with the characters
    for x in range(0, 10):
        for y in range(0, 10):
            # border character (#) is when y == 0, y == 9, x == 1, x == 9
            if (x == 0) or (x == 9) or (y == 0) or (y == 9):
                grid[x].append("#")
            else:
                grid[x].append("-")

    # print the grid line-by-line instead of using print in one line
    for x in range(0, 10):
        for y in range(0, 10):
            print(grid[x][y], end="\t")
        print("\n")

play_game()
