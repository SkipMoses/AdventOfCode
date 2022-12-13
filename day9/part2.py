from help import point

file = "input.txt"
with open(file) as f:
    lines = [l.strip().split() for l in f.readlines()]
    f.close()

rope = [point([0,0]) for i in range(10)]

tpath = {(0,0)}

for i in lines:
    d = i[0]
    s = int(i[1])
    while s > 0:
        s -= 1
        rope[0].move(d)
        for j in range(1, len(rope)):
            rope[j].direc(rope[j-1])
        tpath.add(rope[-1].tup())

print(len(tpath))

