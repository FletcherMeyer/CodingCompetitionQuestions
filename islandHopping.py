# grid, width, and height being given through input.
grid = [
    ["L","W","W","W","W"],
    ["L","W","L","W","W"],
    ["W","W","W","W","L"],
    ["L","W","W","W","W"]
]
height = 4;
width = 5;

# Need to check the value to the right, bottom, and right-bottom, starting from tile (0,0).

def checkCell(x, y) :
    # Check to see if the parameters provided meet the requirements given by the grid.
    # Ex: X cannot exceed width size.
    if x == width :
        return;
    if y == height :
        return;
    # Check if the value is water, then no further recursion is necessary.
    if grid[y][x] == "W":
        return;
    
    # If the tile is land, then we will continue to check for other land and replace.
    # Replace it with C, as the value has been checked as a result of an island existing.
    grid[y][x] = "C"

    checkCell(x + 1, y + 1);
    checkCell(x + 1, y);
    checkCell(x, y + 1);

islands = 0;
for y in range(height) :
    for x in range(width) :
        if grid[y][x] == "L" :
            # An unchecked value (new island) has been found.
            islands += 1;
            checkCell(x, y);

print (islands)
