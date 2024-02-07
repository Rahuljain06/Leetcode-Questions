class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        maxFreq = max(freq.values())

        

        # Creating buckets with length of maximum freq+1

        # Note that maxFreq <= len(s)

        buckets = [[] for _ in range(maxFreq+1)]

        for c,f in freq.items():

            buckets[f].append(c)

        

        # Going through the buckets from large freq to small freq to create the result.

        res = []

        for f in reversed(range(maxFreq+1)):

            for c in buckets[f]:

                res.append(c * f)

                

        return "".join(res)