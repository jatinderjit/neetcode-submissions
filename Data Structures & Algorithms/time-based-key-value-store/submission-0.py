from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        vals = self.values.setdefault(key, ([], []))
        vals[0].append(timestamp)
        vals[1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        ts, vals = self.values.get(key, (None, ""))
        if ts is None:
            return ""
        i = bisect_right(ts, timestamp)
        if i == 0:
            return ""
        return vals[i - 1]
