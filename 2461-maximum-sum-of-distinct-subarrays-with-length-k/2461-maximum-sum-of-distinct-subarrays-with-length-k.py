class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        check = set()
        left = 0
        c_sum = 0
        m_sum = 0
        for right in range(0,len(nums)):
            while nums[right] in check or len(check) == k:
                c_sum -= nums[left]
                check.remove(nums[left])
                left +=1
            c_sum +=nums[right] # 1 2
            check.add(nums[right]) # 1 2
            if len(check)==k:
                m_sum = max(c_sum, m_sum)
        return m_sum
        