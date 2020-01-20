import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for col in range(cols)] for row in range(rows)]

    def __repr__(self):
        tstr = f"Matrix<{self.rows}x{self.cols}>["
        for idx, row in enumerate(range(self.rows)):
            if idx == self.rows-1:
                tstr += f"{self.matrix[row]}]"
            else:
                tstr += f"{self.matrix[row]}\n"
        return tstr

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random.randint(0, 100)
    
    @property
    def T(self):
        tm = Matrix(self.cols, self.rows)
        for i in range(tm.rows):
            for j in range(tm.cols):
                tm.matrix[i][j] = self.matrix[j][i]
        return tm


if __name__ == '__main__':
    m = Matrix(2, 3)
    m.randomize()
    print(m)
    print(m.T)