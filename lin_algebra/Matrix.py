class Matrix:
    ''' Class to create and manipulate matrices
    '''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []
        for i in range(rows):
            self.data.append([0] * cols)

    def __str__(self):
        s = ""
        for i in range(self.rows):
            s += "["
            for j in range(self.cols):
                s += str(self.data[i][j]) + " "
            s += "]\n"
        return s

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        else:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        else:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] - other.data[i][j]
            return result

    def __mul__(self, other):
        if self.cols != other.rows:
            return None
        else:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    def get_determinant(self):
        if self.rows != self.cols:
            return None
        else:
            if self.rows == 1:
                return self.data[0][0]
            else:
                result = 0
                for i in range(self.rows):
                    result += (-1)**i * self.data[0][i] * self.get_cofactor(0, i).get_determinant()
                return result
    
    def get_cofactor(self, row, col):
        result = Matrix(self.rows - 1, self.cols - 1)
        for i in range(self.rows):
            if i == row:
                continue
            for j in range(self.cols):
                if j == col:
                    continue
                result.data[i - 1][j - 1] = self.data[i][j]
        return result


    def get_inverse(self):
        if self.rows != self.cols:
            return None
        else:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = ((-1)**(i + j)) * self.get_cofactor(i, j).get_determinant()
            result = result.transpose()
            for i in range(self.rows):
                result.data[i][i] = result.data[i][i] / self.get_determinant()
            return result

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def get_value(self, row, col):
        return self.data[row][col]

    def get_row(self, row):
        return self.data[row]

    def get_col(self, col):
        return [self.data[i][col] for i in range(self.rows)]

    def get_size(self):
        return (self.rows, self.cols)

    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols
    



