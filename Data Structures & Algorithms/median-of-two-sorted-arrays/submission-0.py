class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        total = m + n
        req = (total + 1) >> 1
        if n == 0:
            if m & 1:
                return nums1[req - 1]
            return (nums1[req - 1] + nums1[req]) / 2

        i, j = 1, min(m, req)
        while i <= j:  # Num of elements to pick from num1
            count1 = (i + j) >> 1
            count2 = req - count1
            if count2 > n:
                i = count1 + 1
                continue

            num1, num2 = nums1[count1 - 1], nums2[max(count2 - 1, 0)]
            if count2 == 0:
                if num1 <= num2:
                    if total & 1:
                        return num1
                    if count1 < m:
                        num2 = min(num2, nums1[count1])
                    return (num1 + num2) / 2
                j = count1 - 1
                continue
            elif num1 <= num2:
                if count1 < m and nums1[count1] <= num2:
                    i = count1 + 1
                else:
                    if total & 1:
                        return num2
                    num1 = nums2[count2] if count2 < n else nums1[count1]
                    if count1 < m:
                        num1 = min(num1, nums1[count1])
                    return (num1 + num2) / 2
            else:  # num1 >= num2
                if count2 < n and nums2[count2] <= num1:
                    j = count1 - 1
                else:
                    if total & 1:
                        return num1
                    num2 = nums1[count1] if count1 < n else nums2[count2]
                    if count2 < n:
                        num1 = min(num1, nums2[count2])
                    return (num1 + num2) / 2
