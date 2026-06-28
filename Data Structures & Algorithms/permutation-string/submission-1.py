class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        curr = Counter()
        i = 0
        for j, ch in enumerate(s2):
            if ch not in count:
                i, curr = j + 1, Counter()
                continue
            curr[ch] += 1
            target_count = count[ch]
            while curr[ch] > target_count:
                curr[s2[i]] -= 1
                i += 1
            if j - i + 1 == len(s1):
                return True
        return False
