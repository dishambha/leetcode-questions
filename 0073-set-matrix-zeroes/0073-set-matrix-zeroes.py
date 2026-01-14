class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()

        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(0,m):
            for j in range(0,n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        