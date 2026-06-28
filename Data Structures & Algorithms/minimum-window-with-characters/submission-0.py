class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = Counter()
        i = 0
        min_len = len(s) + 1
        ans = ""
        found = 0
        for j, ch in enumerate(s):
            s_count[ch] += 1
            if s_count[ch] == t_count[ch]:
                found += 1
            while i <= j and (s[i] not in t_count or s_count[s[i]] > t_count[s[i]]):
                s_count[s[i]] -= 1
                i += 1
            if found == len(t_count) and j - i + 1 < min_len:
                ans = s[i:j+1]
                min_len = j - i + 1
        return ans