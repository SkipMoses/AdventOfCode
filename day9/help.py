class point:
    coord = list()
    def __init__(self, x = [0,0]):
        self.coord = x
    def __str__(self):
        return str(self.coord) 

    def __abs__(self):
        return max([abs(i) for i in self.coord])

    def __sub__(self, other):
        temp = [self.coord[i] - other.coord[i] for i in range(2)]
        return point(temp)

    def tup(self):
        return (self.coord[0], self.coord[1])

    def move(self, i):
        if i == 'D':
            self.coord[1] -= 1
        elif i == 'U':
            self.coord[1] += 1
        elif i == 'L':
            self.coord[0] -= 1
        elif i == 'R':
            self.coord[0] += 1

    def direc(self, head):
        temp = head - self
        Q1 = [[1,2], [2,1],[2,2]]
        Q2 = [[-1,2], [-2,1], [-2,2]]
        Q3 = [[-1,-2], [-2,-1], [-2,-2]]
        Q4 = [[1,-2], [2,-1], [2,-2]]
        if temp.coord == [2,0]:
            self.coord[0] += 1
        elif temp.coord == [-2,0]:
            self.coord[0] -= 1
        elif temp.coord == [0, 2]:
            self.coord[1] += 1
        elif temp.coord == [0, -2]:
            self.coord[1] -= 1
        elif temp.coord in Q1:
            self.coord[0] += 1
            self.coord[1] += 1
        elif temp.coord in Q4: 
            self.coord[0] += 1
            self.coord[1] -= 1
        elif temp.coord in Q2: 
            self.coord[0] -= 1
            self.coord[1] += 1
        elif temp.coord in Q3: 
            self.coord[0] -= 1
            self.coord[1] -= 1

