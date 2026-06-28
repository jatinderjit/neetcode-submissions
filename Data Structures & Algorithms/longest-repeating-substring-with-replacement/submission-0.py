class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        i = 0
        counts = Counter()
        max_count = 0
        for j, ch in enumerate(s):
            counts[ch] += 1
            max_count = max(max_count, counts[ch])
            size = j - i + 1
            if size - max_count > k:  # extra chars
                counts[s[i]] -= 1
                i += 1
                size -= 1
            ans = max(ans, size)
        return ans
