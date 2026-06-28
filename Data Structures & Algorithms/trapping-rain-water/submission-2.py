class Solution:
    def trap(self, height: List[int]) -> int:
        hi = hi_idx = -1
        for i, h in enumerate(height):
            if h > hi:
                hi, hi_idx = h, i

        total = 0
        for rng in [range(hi_idx), range(len(height) - 1, hi_idx, -1)]:
            max_h = 0
            for i in rng:
                h = height[i]
                if h >= max_h:
                    max_h = h
                else:
                    total += max_h - h
        return total