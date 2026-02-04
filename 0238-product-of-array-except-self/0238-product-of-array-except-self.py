class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_prod = [1]
        p = nums[0]
        for i in range(1,n):
            pref_prod.append(p)
            p *= nums[i]

        p = nums[-1]
        for i in range(n-2, -1,-1):
            pref_prod[i] *= p
            p *= nums[i]
        return pref_prod