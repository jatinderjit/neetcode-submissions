class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m
        row = None
        while left < right:
            mid = (left + right) // 2
            curr = matrix[mid]
            if target >= curr[0]:
                if target <= curr[-1]:
                    row = curr
                    break
                left = mid + 1
            else:
                right = mid
        if row is None:
            return False

        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            num = row[mid]
            if num == target:
                return True
            if num < target:
                left = mid + 1
            else:
                right = mid
        return False