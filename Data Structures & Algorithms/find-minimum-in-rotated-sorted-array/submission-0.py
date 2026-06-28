class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if i == j or nums[i] < nums[j]:
                return nums[i]
            mid = (i + j) // 2
            if nums[i] <= nums[mid]:
                i = mid + 1
            else:
                j = mid
