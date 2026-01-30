class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_diff = sys.maxsize
        left =0
        c_sum = 0
        for right in range(0, len(nums)):
            c_sum += nums[right]
            while c_sum >=target:
                if (right-left+1):
                    min_diff = min(min_diff, right-left+1)
                c_sum -= nums[left]
                left +=1
        if min_diff == sys.maxsize:
            return 0
        else:
            return min_diff