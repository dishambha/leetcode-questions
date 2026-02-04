class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        rem_index = {0:-1}
        pref_sum=0
        for i in range(n):
            pref_sum += nums[i]
            rem = pref_sum%k
            if rem in rem_index:
                if i-rem_index[rem] >= 2:
                    return True
            else:
                rem_index[rem] = rem_index.get(rem,0)+i
        return False
