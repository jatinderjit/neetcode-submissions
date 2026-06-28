class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        left_width = [None] * n
        stack = [(-1, -1)]
        for i, h in enumerate(heights):
            while h <= stack[-1][0]:
                stack.pop()
            left_width[i] = i - stack[-1][1]
            stack.append((h, i))

        max_area = 0
        stack = [(-1, n)]
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while h <= stack[-1][0]:
                stack.pop()
            width = left_width[i] + stack[-1][1] - i - 1
            max_area = max(max_area, width * h)
            stack.append((h, i))

        return max_area