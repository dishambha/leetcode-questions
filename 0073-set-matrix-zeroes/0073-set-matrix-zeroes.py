class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        column = set()
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    column.add(j)
        for i in range(0,m):
            for j in range(0,n):
                if i in rows or j in column:
                    matrix[i][j] = 0

        