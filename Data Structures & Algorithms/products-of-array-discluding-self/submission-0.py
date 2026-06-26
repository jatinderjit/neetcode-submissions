class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        after = [None] * len(nums)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            after[i] = curr
            curr *= nums[i]

        out = [None] * len(nums)
        curr = 1
        for i, num in enumerate(nums):
            out[i] = curr * after[i]
            curr *= num
        return out
