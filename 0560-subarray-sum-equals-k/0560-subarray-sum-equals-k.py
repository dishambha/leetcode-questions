class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prev_map = {0:1}
        prev_sum = 0
        for i in range(n):
            prev_sum += nums[i]

            if prev_sum-k in prev_map:
                count += prev_map.get(prev_sum-k, 0)
            prev_map[prev_sum] = prev_map.get(prev_sum,0)+1
        return count