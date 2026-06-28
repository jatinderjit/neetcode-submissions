class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n
        while left < right:
            mid = (left + right) // 2
            i, j = divmod(mid, n)
            num = matrix[i][j]
            if num == target:
                return True
            if num < target:
                left = mid + 1
            else:
                right = mid
        return False