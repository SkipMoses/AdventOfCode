import helper as help

# Read input
#file = "test.txt"
file = "input.txt"
with open(file) as f:
    lines = [l.strip() for l in f.readlines()]
    f.close()

forest = [[[int(i), 1, True] for i in l] for l in lines]
forest[3][3][0] = 0 
row = len(forest)
col = len(forest[0])

# Initialize the border flag to true

for r in range(row):
    forest[r][0][2] = False 
    forest[r][0][1] = 0
    forest[r][-1][2] = False 
    forest[r][-1][1] = 0

for c in range(col):
    forest[0][c][2] = False
    forest[0][c][1] = 0
    forest[-1][c][2] = False
    forest[-1][c][1] = 0


Views = [[t for t in forest],
         help.rotateN([t for t in forest],3),
         help.rotateN([t for t in forest],2),
         help.rotateN([t for t in forest])
         ]

for T in Views:
    for r in T:
        help.scoreRow(r)

for i in range(4):
    Views[i] = help.rotateN(Views[i], i)


P = [[Views[0][r][c][1]*Views[1][r][c][1]*Views[2][r][c][1]*Views[3][r][c][1] for c in range(col)] for r in range(row)]

m = 0
for r in range(row):
    for c in range(col):
        if P[r][c] > m:
            m = P[r][c]
print(m)

