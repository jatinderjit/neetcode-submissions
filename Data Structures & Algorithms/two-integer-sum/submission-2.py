class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        i, j = 0, len(nums) - 1
        while i != j:
            curr = nums[i][1] + nums[j][1]
            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                return sorted([nums[i][0], nums[j][0]])