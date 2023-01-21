class Solution(object):
#    def restoreIpAddresses(self, s: str) -> List[str]:
#         rst = []
#         self.backtrack(s, 0, '', rst)
#         return rst
#     def backtrack(self,s, dots, path, rst):
#         if dots == 4:
#             #have 4 chunk and all the digits are used than we append
#             if not s: rst.append(path[:-1]) # we are excluding the 4 and last dot here"255.255.11.135."
#             return
#         for i in range(1, 4):
#             #prevent index overflow
#             if i > len(s):
#                 continue
#             #take 1 digit is always good
#             #take 2 or 3 digits, first digit cannot be '0'
#             if i > 1 and s[0] == '0':
#                 continue
#             #take 3 digits, cannot greater than 255
#             if i > 2 and int(s[:3]) > 255:
#                 continue
#             self.backtrack(s[i:], dots+1, path + s[:i] + '.', rst)
            
            
            
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx > 4:
            return
        #have 4 chunk and all the digits are used than we append
        if idx == 4 and not s:
            res.append(path[:-1]) # we are excluding the 4 and last dot here"255.255.11.135."
            return 
        for i in range(1, len(s)+1):
            # agr single 0 ke baad point . lag rha hai to thik hai par 0 ke baad koi no. hai or fir point . lag rha hai to galat hai 01. #cc: question
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)      