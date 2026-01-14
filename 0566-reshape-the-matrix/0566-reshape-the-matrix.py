class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        flat_mat =[]
        final_res = []
        for i in range(0,m):
            for j in range(0,n):
                flat_mat.append(mat[i][j])

        if m*n != c*r:
            return mat
        leng = len(flat_mat)
        res =[]
        for i in range(0,leng,c):
            res = flat_mat[i:i+c]
            final_res.append(res)
        return final_res


