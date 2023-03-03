class Solution:
    def strStr(self, s: str, n: str) -> int:
        for i in range(len(s) - len(n)+1):
            if s[i:i+len(n)] == n:
                return i
        return -1



            