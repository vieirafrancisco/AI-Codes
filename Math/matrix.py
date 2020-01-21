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

    def __add__(self, other):
        m = Matrix(self.rows, self.cols)
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise Exception("Matricies order down't match!")
            for i in range(self.rows):
                for j in range(self.cols):
                    m.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        elif isinstance(other, int):
            for i in range(self.rows):
                for j in range(self.cols):
                    m.matrix[i][j] = self.matrix[i][j] + other
        else:
            raise Exception("Can't add this element!")
        return m

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols == other.rows:
                m = Matrix(self.rows, other.cols)
            else:
                raise Exception("Can't multiply matricies with cols != rows")
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        m.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        elif isinstance(other, int):
            m = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    m.matrix[i][j] = self.matrix[i][j] * other
        else:
            raise Exception("Can't add this element!")
        return m

    def randomize(self, n=100):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random.randint(0, n)

    @property
    def T(self):
        tm = Matrix(self.cols, self.rows)
        for i in range(tm.rows):
            for j in range(tm.cols):
                tm.matrix[i][j] = self.matrix[j][i]
        return tm


if __name__ == '__main__':
    m = Matrix(2, 3)
    m2 = Matrix(3, 2)
    m.randomize(5)
    m2.randomize(5)
    print(m)
    print(m2)
    print(m * m2)
    print("------------")
    print(m + m)
    print((m + m).T + 5)