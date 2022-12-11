# Print contents of A as 
# string
def printArray(A, i):
    print("-------------------------------")
    for r in range(len(A)):
        l = ""
        for c in range(len(A[0])):
            l = l + str(A[r][c][i])
        print(l)
    print("-------------------------------")

# Rotate array 90 degrees 
def rotate(A):
    row = len(A)
    col = len(A[0])
    rA = [[A[-r][c].copy() for r in range(1, row+1)] for c in range(col)]
    return rA

def rotateN(A, N = 1):
    rA = A
    for i in range(N):
        rA = rotate(rA)
    return rA

def scoreRow(R):
    for r in range(1,len(R)-1):
        prior = R[r-1]
        while R[r][0] > prior[0] and prior[2]:
            R[r][1] += prior[1]
            prior = R[r-R[r][1]]

