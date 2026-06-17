import random

grid = []

# if snake is in the boundaries, or in itself, game ends, and return score. if snake is in the apple, increment score
def snake_legal(grid, score):
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
    score = 0

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

    # put snake in a random spot
    snakePos = [
        random.randint(1, 8), random.randint(1, 8)
    ]

    grid[snakePos[0]][snakePos[1]] = "%"

    # add apple in a random spot in the grid that isnt the snake, or the player wins
    placedApple = False

    applePool = []

    for x in range(0, 10):
        for y in range(0, 10):
            if grid[x][y] == "-":
                applePool.append([x, y])

    if len(applePool) > 0:
        randomApplePos = applePool[random.randint(0, len(applePool) - 1)]

        grid[randomApplePos[0]][randomApplePos[1]] = "@"

    print_grid()

    while True:
        player_input = ""

        while player_input not in ["W", "A", "S", "D", "E"]:
            player_input = input(f"Score: {score}\nEnter W, A, S, or D to move the snake (snake body: %) or E to exit: ").upper()

        currentRow, currentCol = snakePos

        next_position = [
            currentRow, currentCol
        ]

        if player_input == "W":
            next_position = [
                currentRow - 1, currentCol
            ]
        elif player_input == "A":
            next_position = [
                currentRow, currentCol - 1
            ]
        elif player_input == "S":
            next_position = [
                currentRow + 1, currentCol
            ]
        elif player_input == "D":
            next_position = [
                currentRow , currentCol + 1
            ]
        elif player_input == "E":
            print(f"Final score: {score}")
            return

        nextRow, nextCol = next_position

        # check if snake made an illegal move (boundary #, or itself %)
        next_grid = grid[nextRow][nextCol]

        if next_grid in ["#", "%"]:
            print(f"Illegal move. Final score: {score}")
            return

        # if snake's next move is in an apple (@), increment score

        if next_grid == "@":
            print("snake will eat an apple")
            score = score + 1

            # snake body will grow and add a body part (%) from its current position
            grid[currentRow][currentCol] = "%"
        else:
            grid[currentRow][currentCol] = "-"

        grid[nextRow][nextCol] = "%"

        snakePos = [
            nextRow, nextCol
        ]

        # update grid

        print_grid()


play_game()
