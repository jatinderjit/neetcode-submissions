class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append(":")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        while s:
            size, s = s.split(":", 1)
            size = int(size)
            decoded.append(s[:size])
            s = s[size:]
        return decoded