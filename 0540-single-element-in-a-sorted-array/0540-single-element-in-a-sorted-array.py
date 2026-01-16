class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = (hi+lo)//2
            if mid%2==0:
                if nums[mid] == nums[mid+1]:
                    lo = mid+2
                else:
                    hi = mid-1
            else:
                if nums[mid] == nums[mid-1]:
                    lo = mid+1
                else:
                    hi = mid-1
        return nums[lo]

'''
nums = [1,1,2,3,3,4,4,8,8]
idx  =  0,1,2,3,4,5,6,7,8

pairs before the single eement{
    (0,1)
}
pairs after the single elements{
    (3,4),
    (5,6),
    (7,8)
}

'''

            