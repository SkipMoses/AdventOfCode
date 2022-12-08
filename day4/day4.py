with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    f.close()

lines = [[line.split(',')[0].split('-'), 
          line.split(',')[1].split('-')] for line in lines]
lines = [l[0] + l[1] for l in lines]

def computeSign(T):
    L = [int(t) for t in T] 
    val = (L[0] - L[2])*(L[1] - L[3])
    return(val <= 0)

#print(sum([computeSign(l) for l in lines]))

def isOverlap(T):
    L = [int(t) for t in T]

    if L[2] < L[0]:
        temp = L[0]
        L[0] = L[2]
        L[2] = temp
        temp = L[1]
        L[1] = L[3]
        L[3] = temp
    if L[2] > L[1]:
        return(False)
    else:
        return(True)

print(sum([isOverlap(T) for T in lines]))

