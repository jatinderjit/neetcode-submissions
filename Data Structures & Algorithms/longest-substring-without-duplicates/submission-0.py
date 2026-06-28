class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        i = 0
        longest = 0
        for j, ch in enumerate(s):
            if ch in chars:
                while s[i] != ch:
                    chars.remove(s[i])
                    i += 1
                chars.remove(s[i])
                i += 1
            chars.add(ch)
            longest = max(longest, j - i + 1)
        return longest
