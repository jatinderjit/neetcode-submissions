class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            num = nums[mid]
            if num == target:
                return mid
            if num > target:
                right = mid
            else:
                left = mid + 1
        return -1