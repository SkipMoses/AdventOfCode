file = "test.txt"

with open(file) as f:
    lines = [l.strip() for l in f.readlines()]
    f.close()

def check(i, c, v):
    ++i
    if i%40 == 20:
        v += c

cycle = 0 
cur = 1
ans = 0
for l in lines:
    if l == "noop":
        check(cycle, cur, ans)
        print(cycle)
    else:
        val = int(l[4:])
        for i in range(2):
            check(cycle, cur, ans)
            print(cycle)
        cur += val

print(ans)
