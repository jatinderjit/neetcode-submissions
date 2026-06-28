class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            hi, hj = heights[i], heights[j]
            max_area = max(max_area, (j - i) * min(hi, hj))
            if hi <= hj:
                i += 1
                if hi == hj:
                    j -= 1
            else:
                j -= 1
        return max_area