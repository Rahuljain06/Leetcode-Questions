class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
         # ham isme maximium kitna square stretch kar sakte hai waise sochenge to pehli baat to maximum points jo square ke andar possible hai vo only 26 hai kyunki a-Z=26 or ha ek tag ka ek point hi square ke andar le sakte hai. To ham maximum distance lenge ek point ke coordinates (x,y) ka and fir uske saamne tag daal denge. fir ham sort kar denge dictionary ko or apna square bada karne ki koshish karenge..or ham ek visited ka set() bana lenge jiske andar tags rahenge to for eg ham distance 1 par hai to hamne uske tags visited me daal diye or phir ham distance 2 pe gaye or hame koi tag visited me mila to ham 1 return kar denge directly kyunki 2 same tag square ke andar nhi ho skta
        N=len(points)
        d=defaultdict(list)
        for (x,y),i in zip(points,s):
            d[max(abs(x),abs(y))].append(i)
        visited=set()
        count=0
        for r in sorted(d): # hamne yaha sort esiliye kiya jisse distance sorted ho jaye or ham square stretch kar paaye
            for t in d[r]:
                if t in visited: # agar koi bhi tag repeat hua to ham usse jyada square stretch nhi kar sakte to hamne ans return kar diya
                    return count
                visited.add(t)
            count+=len(d[r]) # hamne jitne bhi tag particular length ke vo count kar liye agar koi bhi tag repeated nhi hai to
        return count
            
            
        