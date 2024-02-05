class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # iss question me 3 cases hai:
        # 1: jab p[j+1]=="*" ho 
            #iss case ke liye 2 option use and not use
                # use ham tabhi kar sakte jab 2 string match ho (s[i]==p[j]) to ham s wali string badayenge par j wale ko nhi kyunki ham uske * ko agli baar bhi use kar sakte hai.
                # not use karenge to simply hame p[j] wali string ko +2 karna hai jisse current character and agla character * skip ho jaye.
        
        # 2: jab p[j]=="." ho
            # jab p[j] par . hoga to vo koi bhi s[i] ki character se match hoga to hame usko alag se handle karne ki jaroorat nhi hai. vo simple match wale case me #3 case me aa jyega
        # 3: jab s[i]==p[j] ho
            # jab current index par 2 character match ho to simply i and j dono me aage bad jana hai 
        # Important: hamne i>=len(s) par False esiliye nhi kiya kyunki ho sakta hai ki p me extra characters ho with * to jaroori nhi ki ham s khatam ho jaye to ham directly False return kar de. 
        #Eg s="a" p="a*b*" to iska ans true ana chaiye kyunki ham isme b* ko ek baar bhi nhi lenge and a* ko ek baar lenge to esiliye tab ham poori string kar check kar lenge tab hi to return karenge.
    
        dp={}
        def dfs(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            
            match= i<len(s) and (s[i]==p[j] or p[j]==".")
            if (j+1) <len(p) and p[j+1]=="*":
                dp[(i,j)]= (dfs(i,j+2) or #not use *
                      (match and dfs(i+1,j))) #use *
                return dp[(i,j)]
            if match: #
                dp[(i,j)]=dfs(i+1,j+1)
                return dp[(i,j)]
            dp[(i,j)]= False
            return dp[(i,j)]
        return dfs(0,0)
                    
            
            
            
            