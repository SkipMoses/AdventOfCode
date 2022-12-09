# Read in test
#with open("test.txt") as f:
#    inst = [l.strip() for l in f.readlines()]
#    f.close()

# Read in input
with open("input.txt") as f:
    inst = [l.strip() for l in f.readlines()]
    f.close()

val  = [0]
store = [] 

# skip the first root dir call since i already init
inst = inst[1:]
#inst2 = inst[1:]

for i in range(len(inst)):
    if inst[i] == "$ ls" or inst[i][0] == "d":
        continue
    elif inst[i] == "$ cd ..":
        # pop cur from path and put it in stora if < 10000e
        tmp = val.pop()
        if tmp <= 100000:
            store.append(tmp)
        # move up in path 
    elif ord(inst[i][0]) != 36: # file size
        s = inst[i].split()[0]
        val = [v + int(s) for v in val]
    else: # moving into subfolder
        val = val + [0]
# Check in val if there are any files that don't get popped

for v in val:
    if v <= 100000:
        store.append(v)
print(sum(store))

# Part 2
# Basically, we need to remove the bound of 100k and 
# record the file names in a new list

val = [(0, '/')]
store = []

for i in range(len(inst)):
    if inst[i] == "$ ls" or inst[i][0] == "d":
        continue
    elif inst[i] == "$ cd ..":
        # pop cur from path and put it in stora if < 10000e
        tmp = val.pop()
        store.append(tmp)
        # move up in path 
    elif ord(inst[i][0]) != 36: # file size
        s = inst[i].split()[0]
        val = [(v[0] + int(s), v[1])  for v in val]
    else: # moving into subfolder
        s = inst[i].split()
        val = val + [(0, s[2])]

# Combine val and store, sum to find total
max_size = 70000000
need = 30000000
files = val + store
total = files[0][0] 
need = need - (max_size - total)

# Sort files and find the file smalles file bigger than need
files.sort()
for f in files:
    if need < f[0]:
        print(f[0])
        break




