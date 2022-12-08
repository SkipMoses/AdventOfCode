# Read in the input
with open('input.txt') as f:
    line = f.readlines()
    f.close()
# Add \n to help with stopping condition
line.append("\n")

# Part 1 
big = 0
cur = 0 
for l in line:
    if l == "\n": # stop summing and compare
        if cur > big: # New largest found
            big = cur
        cur = 0
    else:
        cur = cur + int(l)

print(big)

# Part 2
big = [0, 0, 0]
cur = 0
for l in line:
    if l == "\n" :
        if cur > big[0]:
            big[2] = big[1]
            big[1] = big[0]
            big[0] = cur
        elif cur > big[1]:
            big[2] = big[1]
            big[1] = cur
        elif cur > big[2]:
            big[2] = cur
        cur = 0
    else:
        cur = cur + int(l)
print(sum(big))
