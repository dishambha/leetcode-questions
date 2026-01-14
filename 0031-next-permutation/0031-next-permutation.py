class Solution:
    def reverse_list(self,start,end,nums):
        while start<end:
            nums[start],nums[end] = nums[end], nums[start]
            start +=1
            end -= 1
        return nums
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)-1
        pivot = -1
        for i in range(n,0,-1):
            if nums[i] > nums[i-1]:
                pivot = i-1
                break
        if pivot == -1:
            self.reverse_list(0,n,nums)
            return
        for j in range(n,pivot,-1):
            if nums[j] > nums[pivot]:
                nums[j], nums[pivot] = nums[pivot], nums[j]
                break
        self.reverse_list(pivot+1,n,nums)
        return