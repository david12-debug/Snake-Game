import random

# game uses a 2D matrix
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
                 
# print the grid line-by-line instead of using print in one line
def print_grid ():
    for x in range(0, 10):
        for y in range(0, 10):
            print(grid[x][y], end="\t")
        print("\n")

# add apple in a random spot in the grid that isnt the snake, or the player wins
def add_apple ():

    applePool = []

    foundApple = False

    for x in range(0, 10):
        for y in range(0, 10):
            if grid[x][y] == "-":
                applePool.append([x, y])
            elif grid[x][y] == "@":
                foundApple = True

    if len(applePool) > 0:
        if foundApple == False:
            randomApplePos = applePool[random.randint(0, len(applePool) - 1)]

            grid[randomApplePos[0]][randomApplePos[1]] = "@"

        return True
    else:
        return False

# creates a clear grid
def clear_grid (grid):
    for x in range(0, 10):
        for y in range(0, 10):
            # border character (#) is when y == 0, y == 9, x == 1, x == 9
            if (x == 0) or (x == 9) or (y == 0) or (y == 9):
                grid[x].append("#")
            else:
                grid[x].append("-")

# set up game loop
def play_game ():
    score = 0

    ended = False

    # add arrays inside grid
    for x in range(0, 10):
        grid.append([])

    # set up grid with the characters
    clear_grid (grid)

    # keep track of the snake's body
    snakeBody = []

    while True:
        # if there isnt a snake position yet, set up snake
        if len(snakeBody) == 0:
            # put snake in a random spot
            randomRow, randomCol = [random.randint(1, 8), random.randint(1, 8)]

            grid[randomRow][randomCol] = "%"

            snakeBody.append([randomRow, randomCol])

        # if there is no apple in the grid, attempt to add an apple in a random spot in the grid that isnt the snake, but if it fails to the player wins
        placedApple = add_apple()

        if placedApple == False:
            print(f"You win! Final score: {score}")

        # display grid to the player
        print_grid()

        # listen to player input
        player_input = ""

        while player_input not in ["W", "A", "S", "D", "E"]:
            player_input = input(f"Score: {score}\nEnter W, A, S, or D to move the snake (snake body: %) or E to exit: ").upper()

        # translate player input to snake movement
        currentRow, currentCol = snakeBody[0]

        # get the snake's incoming position
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
        
        # loop through the snake's body and update their positions

        previousBodyPosition = []

        for i, bodyPosition in enumerate(snakeBody):
            bodyRow, bodyCol = bodyPosition

            # if its the head, just move it to the next position
            if i == 0:
                snakeBody[i] = [nextRow, nextCol]

                grid[nextRow][nextCol] = "%"
            else:
                # body part goes to the old position of the body part before it
                prevRow, prevCol = previousBodyPosition

                snakeBody[i] = [prevRow, prevCol]

                grid[prevRow][prevCol] = "%"

            previousBodyPosition = [bodyRow, bodyCol]

            # hide old body part position
            grid[bodyRow][bodyCol] = "-"

        # if snake's next move is in an apple (@), increment score
        if next_grid == "@":
            score += 1

            # record and add the snake's new body part
            prevRow, prevCol = previousBodyPosition

            snakeBody.append([prevRow, prevCol])

            grid[prevRow][prevCol] = "%"

play_game()
