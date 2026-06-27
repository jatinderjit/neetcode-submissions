class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            curr = numbers[i] + numbers[j]
            if curr <= target:
                if curr == target:
                    return [i + 1, j + 1]
                i += 1
            else:
                j -= 1