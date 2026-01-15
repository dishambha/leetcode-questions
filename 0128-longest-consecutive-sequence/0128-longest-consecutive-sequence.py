class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0,3,7,2,5,8,4,6,0,1]
        n = len(nums)
        if n == 0:
            return 0
        count = 1
        max_count = 1
        nums.sort()
        # 0 0 1 2 3 4 5 6 7 8
        # count = 1
        # max_count = 1
        for i in range(0,n-1): # i =0, 1, 2
            if nums[i] == nums[i+1]: # 0==0, 0 == 1 1==2 2==3
                continue
            elif nums[i]+1 == nums[i+1]: # 0 == 1 , 1==2 
                count += 1 # count = 2, 3
                max_count = max(count,max_count) # 2 3
            else :
                count = 1
        return max_count