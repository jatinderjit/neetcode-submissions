class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        total = 0
        i, j = 0, len(height) - 1
        while i <= j:
            left, right = height[i], height[j]
            if left_max <= right_max:
                left_max = max(left_max, left)
                total += left_max - left
                i += 1
            else:
                right_max = max(right_max, right)
                total += right_max - right
                j -= 1
        return total