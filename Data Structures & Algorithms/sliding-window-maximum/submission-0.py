class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, num in enumerate(nums):
            while q and q[-1][0] < num:
                q.pop()
            q.append((num, i))
            if i >= k - 1:
                ans.append(q[0][0])
                if q[0][1] == i - k + 1:
                    q.popleft()
        return ans
