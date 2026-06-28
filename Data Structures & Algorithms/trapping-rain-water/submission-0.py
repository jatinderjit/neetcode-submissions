class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        total = 0
        i, j = 0, len(height) - 1
        while i <= j:
            left, right = height[i], height[j]
            if left >= left_max:
                left_max = left
                i += 1
            elif right >= right_max:
                right_max = right
                j -= 1
            elif left_max <= right_max:
                total += left_max - left
                i += 1
            else:
                total += right_max - right
                j -= 1
        return total