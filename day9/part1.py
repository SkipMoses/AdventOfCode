from help import point

file = "input.txt"

with open(file) as f:
    lines = [l.strip().split() for l in f.readlines()]
    f.close()


h = point([0,0])
t = point([0,0])
tpath = {t.tup()}
for i in lines:
    direction = i[0]
    steps = int(i[1])
    while steps > 0:
        h.move(direction)
        t.direc(h)
        tpath.add(t.tup())
        steps -= 1

print(len(tpath))
