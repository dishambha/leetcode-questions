class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0,n):
            for j in range(i+1,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for k in range(0,n):
            i = 0
            j = n-1
            while i<=j:
                temp2 = matrix[k][i]
                matrix[k][i] = matrix[k][j]
                matrix[k][j] = temp2
                i +=1
                j -=1
        