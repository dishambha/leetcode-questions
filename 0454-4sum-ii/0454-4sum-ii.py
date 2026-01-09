class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sumAB = {}
        for a in A:
            for b in B:
                s = a+b
                sumAB[s] = sumAB.get(s,0)+1
        count = 0
        for c in C:
            for d in D:
                target = -(c+d)
                if target in sumAB:
                    count += sumAB[target]
        return count

