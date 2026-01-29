class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_area = 0
        max_area = 0
        i = 0
        j = len(height)-1
        while(i<j):
            if height[i] > height[j]:
                curr_area = (j-i) * height[j]
                max_area = max(max_area, curr_area)
                j = j-1
            else:
                curr_area = (j-i) * height[i]
                max_area = max(max_area, curr_area)
                i = i+1
        return max_area     