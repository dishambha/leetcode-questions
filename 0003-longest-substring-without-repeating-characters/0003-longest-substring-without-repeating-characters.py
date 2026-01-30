class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_max, m_max, left= 0,0,0
        check = set()
        for i in range(0,len(s)):
            while s[i] in check:
                c_max -= 1 
                check.remove(s[left])
                left +=1
            c_max +=1
            check.add(s[i])
            m_max = max(c_max,m_max)
        return m_max