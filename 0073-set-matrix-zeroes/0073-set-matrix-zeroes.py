class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        row = set()
        cols = set()
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    row.add(i)
                    cols.add(j)
        for i in range(0,m):
            for j in range(0,n):
                if i in row or j in cols:
                    matrix[i][j] = 0
        