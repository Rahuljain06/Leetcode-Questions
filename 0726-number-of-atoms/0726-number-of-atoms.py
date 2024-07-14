class Solution:
    def countOfAtoms(self, f: str) -> str:
        st=[defaultdict(int)]
        i=0
        while i<len(f):
            if f[i]=="(":
                st.append(defaultdict(int))
            elif f[i]==")":
                cur_map=st.pop()
                count=""
                while i+1<len(f) and f[i+1].isdigit():
                    count+=f[i+1]
                    i+=1
                count=1 if count=="" else int(count)
                pre_map=st[-1]
                for val in cur_map:
                    pre_map[val]+=cur_map[val]*count
            
            else:
                element=f[i]
                if i+1<len(f) and f[i+1].islower():
                    element=f[i:i+2]
                    i+=1
                count=""
                while i+1<len(f) and f[i+1].isdigit():
                    count+=f[i+1]
                    i+=1
                count=1 if count=="" else int(count)
                cur_map=st[-1]
                cur_map[element]+=count
            i+=1
        cur_map=st[-1]
        res=""
        for val in sorted(cur_map.keys()):
            count=cur_map[val] if cur_map[val]!=1 else ""
            res+=val+str(count)
        return res

                    
                
                