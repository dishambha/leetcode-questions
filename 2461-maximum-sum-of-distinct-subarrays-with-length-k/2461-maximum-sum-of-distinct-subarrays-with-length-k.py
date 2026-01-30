class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        check = set()
        c_sum, m_sum, left = 0,0,0
        for right in range(0,len(nums)):
            while nums[right] in check or len(check) == k:
                check.remove(nums[left])
                c_sum -= nums[left]
                left += 1
            c_sum += nums[right]
            check.add(nums[right])
            if len(check) == k:
                m_sum = max(c_sum, m_sum)
        return m_sum
        
