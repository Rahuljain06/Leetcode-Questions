class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        # if len(word)==k or len(word)==1:
        #     return 0
        # d = defaultdict(int)
        # for i in range(0,len(word), k):
        #     d[word[i:i+k]] += 1
        # maxi = max(d.values())
        # return len(word) // k - maxi

        if len(word)==k or len(word)==1:
                    return 0
        d=defaultdict(int)
        maxi=0
        for i in range(0,len(word),k):
            w1=word[i:i+k]
            d[w1]+=1
        maxi=max(d.values())
        return len(word)//k-maxi