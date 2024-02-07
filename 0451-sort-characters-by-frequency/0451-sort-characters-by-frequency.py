class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        s=sorted(s,key=lambda x:(-cnt[x], x))
        return "".join(s)