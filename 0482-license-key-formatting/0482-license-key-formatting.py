class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1] # we are reversing it beacuse in the question it is mentioned there shoudl be atleast one character in the first group.
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
                
                
                