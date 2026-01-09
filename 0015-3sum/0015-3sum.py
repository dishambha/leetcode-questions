class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(0,n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                fin_res = nums[i]+nums[left]+nums[right]
                if fin_res == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left = left+1
                    right = right-1
                    while left<right and nums[left] == nums[left-1]:
                        left = left+1
                    while left<right and nums[right] == nums[right+1]:
                        right = right-1
                elif fin_res < 0:
                    left+=1
                else:
                    right-=1
        return res

        