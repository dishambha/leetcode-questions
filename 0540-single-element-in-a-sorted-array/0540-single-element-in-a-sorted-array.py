class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n =len(nums)-1
        i = 0
        ans = -1
        while i<n:
            if nums[i] == nums[i+1]:
                i +=2
            elif nums[i] != nums[i+1]:
                ans = nums[i]
                break
        if ans == -1:
            return nums[n]
        else:
            return ans
            