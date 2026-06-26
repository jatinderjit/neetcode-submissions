class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [(count, num) for (num, count) in Counter(nums).items()]
        most_freq = heapq.nlargest(k, counts)
        return [num for _, num in most_freq]