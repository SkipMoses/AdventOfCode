with open("input.txt") as f:
    lines = [l.replace(' ', '-').strip() for l in f.readlines()]
    f.close()

stacks = lines[:8]
inst = lines [10:]

#stacks = lines[:3]
#inst = lines[5:]

q = [[] for i in range(9)]

#q = [[] for i in range(3)]

#Extract cargo stack data
for s in range(len(stacks)):
    cur = stacks[-s-1]
    j = 0
    for i in range(1,35,4):
    #for i in range(1,11,4):
        item = cur[i]
        if item != '-':    
            q[j].append(item)
        j = j + 1

for i in q:
    print(i)

#Extract instructions

inst = [l.split('-') for l in inst]
inst = [[int(l[1]), int(l[3]), int(l[5])] for l in inst]

def moveCrate(S, I):
    count = I[0]
    start = I[1]
    end = I[2]
    while count > 0:
        S[end-1].append(S[start-1].pop())
        count = count - 1
    return(S)

#for i in inst:
#    q = moveCrate(q, i)

def moveCrates(S, I):
    count = I[0]
    s = I[1]
    e = I[2]
    S[e-1] = S[e-1] + S[s-1][len(S[s-1]) - count:]
    S[s-1] = S[s-1][:len(S[s-1]) - count]
    return(S)

for i in inst:
    q = moveCrates(q,i)

for i in q:
    print(i[-1])
