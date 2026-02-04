class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [nums[0]]
        for i in range(1,n):
            pref.append(pref[i-1]+nums[i])
        total_sum = pref[-1]

        for i in range(n):
            left_sum = pref[i-1] if i > 0 else 0
            right_sum = total_sum - pref[i]

            if left_sum == right_sum:
                return i
        return -1