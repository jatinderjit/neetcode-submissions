class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            groups[key].append(s)
        return list(groups.values())