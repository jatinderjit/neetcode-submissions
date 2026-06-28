class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(Counter(nums).items())
        ans = []
        for i, (x, xc) in enumerate(nums):
            j = i + 1 if xc == 1 else i
            k = len(nums) - 1
            while j <= k:
                y, yc = nums[j]
                z, zc = nums[k]
                if j == k:
                    yc -= 1
                    if i == j:
                        yc -= 1
                    if yc <= 0:
                        break
                curr = x + y + z
                if curr <= 0:
                    if curr == 0:
                        ans.append([x, y, z])
                        j, k = j + 1, k - 1
                    else:
                        j += 1
                else:
                    k -= 1
        return ans