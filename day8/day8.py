# Part 1
def findTrees(A):
    grid = A
    row = len(grid)
    col = len(grid[0])
    for r in range(1, row-1):
        for c in range(1, col-1):
            # Compare height of tree to tallest north of it
            height = grid[r][c][0]
            top = grid[r-1][c][1]
            if height > top:
                print("Visible tree found at " + str(r) + str(c))
                grid[r][c][1] = height
                grid[r][c][2] = 1
            else:
                grid[r][c][1] = top
    # Reset for next pass
    for r in range(1, row-1):
        for c in range(1, col-1):
            grid[r][c][1] = 0
    return grid

def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


# Import text files
with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    f.close()

grid = []
for l in lines:
    # Each tree in the forest holds it's value
    # The largest peak to the left and top 
    # and a flag indicating if it is a visible  
    tmp = [[int(i), 0, 0] for i in l]
    grid.append(tmp)

# Initialize grid so the borders are set to visibile
row = len(grid)
col = len(grid[0])

for c in range(col):
    # Set the largest tree from the top to the border tree
    grid[0][c][1] = grid[0][c][0]
    grid[0][c][2] = 1 
    # Set the last row
    grid[-1][c][1] = grid[-1][c][0]
    grid[-1][c][2] = 1

for r in range(row):
    # Set left border to be visible
    grid[r][0][1] = grid[r][0][0]
    grid[r][0][2] = 1 

    # Set the right side 
    grid[r][-1][1] = grid[r][-1][0]
    grid[r][-1][2] = 1 


for i in range(4):
    grid = findTrees(grid)
    grid = rotate_matrix(grid)

print(sum([sum([i[2] for i in g]) for g in grid]))

