import random
import time
import copy

WIDTH = 90  # Specifies the width of the window as a constant value
HEIGHT = 90  # Specifies the height of the window as a constant value

# Create a nested list for the cells
cells = []
for x in range(WIDTH):
    column = []  # Creates a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # Add a living cell.

        else:
            column.append(' ')  # Add a dead cell.
    cells.append(column)  # The cells list is a list of column lists

while True:  # Main program loop
    print('\n\n\n\n\n')  # Separate each step with newlines
    current_cells = copy.deepcopy(cells)

    # Print current_cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')  # Prints either a dead or
            # living cell
        print()  # Prints a newline at the end of each row.

    # Calculate the next step's cells based on the current step's cell:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring coordinates:
            # '% WIDTH` ensures the coordinates is always between 0 & WIDTH - 1
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # Tally the number of living cells/neighbours
            neighbours = 0
            if current_cells[left_coord][above_coord] == '#':
                neighbours += 1  # Top-left cell is alive
            if current_cells[x][above_coord] == '#':
                neighbours += 1  # Top neighbour is alive
            if current_cells[right_coord][above_coord] == '#':
                neighbours += 1  # Top right neighbour is alive
            if current_cells[left_coord][y] == '#':
                neighbours += 1  # Left neighbour is alive
            if current_cells[right_coord][y] == '#':
                neighbours += 1  # Right neighbour is alive
            if current_cells[left_coord][below_coord] == '#':
                neighbours += 1  # Bottom-left neighbour is alive
            if current_cells[x][below_coord] == '#':
                neighbours += 1  # Bottom neighbour is alive
            if current_cells[right_coord][below_coord] == '#':
                neighbours += 1  # Bottom-left neighbour is alive

            # Set cell based on Conway's Game of Life Rules:
            if current_cells[x][y] == '#' and (neighbours == 2 or neighbours
                                               == 3):
                # Living cells with 2 or 3 neighbours stay alive:
                cells[x][y] = '#'
            elif current_cells == ' ' and neighbours == 3:
                # Dead cells with 3 neighbours become alive:
                cells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                cells[x][y] = ' '
    time.sleep(1)  # Adds a 1 second pause to reduce flickering
