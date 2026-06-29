from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                if nums[i] <= nums[mid]:
                    if target >= nums[i]:
                        k = bisect_left(nums, target, lo=i, hi=mid)
                        if k < mid and nums[k] == target:
                            return k
                        return -1
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if mid + 1 < n and nums[mid + 1] <= nums[j]:
                    if target <= nums[j]:
                        k = bisect_left(nums, target, lo=mid + 1, hi=j + 1)
                        if k <= j and nums[k] == target:
                            return k
                        return -1
                    j = mid - 1
                else:
                    i = mid + 1

        return -1