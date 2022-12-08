with open("test.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    f.close()
bins = [[l[:len(l)//2], l[len(l)//2:]] for l in lines]

def myfunc(e):
    if e.isupper():
        return(ord(e) - 38)
    else:
        return(ord(e) - 96)

bins = [[''.join(sorted(l[:len(l)//2])),
         ''.join(sorted(l[len(l)//2:]))] for l in lines]

def findMatch(a,b):
    p = 0
    q = 0
    while(p < len(a) and  q < len(b)):
        if a[p] == b[q]:
            return(a[p])
        if a[p] > b[q]:
            q = q + 1
        else:
            p = p + 1

def findAllMatches(a,b):
    p = 0
    q = 0
    matches = [1]
    while(p < len(a) and  q < len(b)):
        if a[p] == b[q] and matches[-1] != a[p]:
            matches.append(a[p])
            if p == len(a)-1 or q == len(b)-1:
                break
            p = p + 1
            q = q + 1
        elif a[p] > b[q]:
            q = q + 1
        else:
            p = p + 1
    return(matches[1:])

def findGroup(a,b,c):
    m = findAllMatches(a,b)
    return(findMatch(m,c))

trips = [[''.join(sorted(lines[i])),
          ''.join(sorted(lines[i+1])),
          ''.join(sorted(lines[i+2]))] for i in range(0,len(lines), 3)]

result = [findGroup(t[0], t[1], t[2]) for t in trips]

print(sum([myfunc(p) for p in result]))

