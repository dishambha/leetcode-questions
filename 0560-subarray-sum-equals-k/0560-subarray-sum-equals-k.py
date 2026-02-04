class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        h_map = {0:1}
        Sum = 0
        for i in range(0,n):
            Sum += nums[i]
            if Sum-k in h_map:
                count += h_map.get(Sum-k,0)
            h_map[Sum] = h_map.get(Sum,0)+1

        return count
