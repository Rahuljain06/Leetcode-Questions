class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #isme ham 0 par True save kar ke starting se chal rhe hai fir word le rhe hai ek ek karke or i-len(w) par check kar rhe hai agar vo word string me i-len(w):i tak basically string ke utne portion ki lenggth jitna word ki length or agar vo dono equal hai to ham waha True save kar denge or ham ye continue karte jaayenge or fir last me agar True rha matlab wordict ke words se exactly string bani hai
        
        
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1,n+1):
            for w in wordDict:
                if i-len(w)>=0 and dp[i-len(w)] and s[i-len(w):i]==w:
                    dp[i]=True
                    break
        return dp[-1]
        
        
        
        
#         The idea is the following:

# d is an array that contains booleans

# d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

# Example:

# s = "leetcode"

# words = ["leet", "code"]

# d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

# d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

# The result is the last index of d.
                
            