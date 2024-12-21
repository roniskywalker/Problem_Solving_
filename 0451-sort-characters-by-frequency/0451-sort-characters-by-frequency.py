class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        buckets = defaultdict(list)
        for char, freq in frequency.items():
            buckets[freq].append(char)
        res = []
        for i in range(len(s), 0, -1):
            if i in buckets:
                for c in buckets[i]:
                    res.append(c * i)
        return "".join(res)