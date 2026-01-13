class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        res =[]
        for i in range(0,n):
            for j in range(0,m):
                res.append(mat[i][j])
        if n*m != r*c:
            return mat
        final_res =[]
        for i in range(0,len(res),c):
            sol = res[i:i+c]
            final_res.append(sol)

        return final_res
