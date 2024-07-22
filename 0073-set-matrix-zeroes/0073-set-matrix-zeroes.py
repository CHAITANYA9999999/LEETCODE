class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isRowZero = True if matrix[0].count(0) != 0 else False
        isColZero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isColZero = True
                break
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        print(matrix)
        
        for j in range(1,len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        if isRowZero:
            matrix[0] = [0]*len(matrix[0])
        if isColZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        return matrix