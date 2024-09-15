class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, e in enumerate(s):
            last_index[e] = i
        res = []
        size, end = 0, 0
        for i, e in enumerate(s):
            size += 1
            end = max(end, last_index[e])
            if i == end:
                res.append(size)
                size = 0
        return res