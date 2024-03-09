class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # iss question me ham basically ham r pointer bada rhe hai tab tak ki windowsize-frequency of max character <=k tak hai kyunki for eg: AABAA k=1 to isme mai longest substring 5 aayegi kyunki isme window size kitni hai= 5 or sabse jyada baar konsa character repeat hua A 4 baar to hame iss window sirf B ko hi to change karna hai or fir ans mil jayega to 5-4<=1 to condition thik hai to chal jayegi or res me ham 5 store kar lenge par agar condition met nhi hogi to ham left ko bada denge or uski character ki frequency ham hashmap se - kar denge or fir max check karenge r badakar ki uss window me condition met ho rhi hai kya and aise last tak check karenge....
        d={}
        l= 0
        res=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            if (r-l+1 - max(d.values()))>k:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            