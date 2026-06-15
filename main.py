import random

grid = []

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

# print the grid line-by-line instead of using print in one line
def print_grid ():
    for x in range(0, 10):
        for y in range(0, 10):
            print(grid[x][y], end="\t")
        print("\n")

# define an empty grid, and set up game loop
def play_game ():

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

    print_grid()

    # put snake in a random spot
    snakePos = [
        random.randint(1, 8), random.randint(1, 8)
    ]

    # add apple in a random spot in the grid that isnt the snake, or the player wins
    placedApple = False

    applePool = []

    for x in range(0, 10):
        for y in range(0, 10):
            if grid[x][y] == "-":
                applePool.append([x, y])

    if len(applePool) > 0:
        randomApplePos = applePool[random.randint(0, len(applePool))]

        grid[randomApplePos[0]][randomApplePos[1]] = "@"

    print_grid()


play_game()
