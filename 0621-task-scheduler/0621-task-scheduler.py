class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Approach:
        
        d=defaultdict(int)
        maxi=0
        noofmaxi=0
        
        for i in tasks:
            d[i]+=1
            if d[i]==maxi:
                noofmaxi+=1
            elif d[i]>maxi:
                noofmaxi=1
                maxi=d[i]
        
        partcount=maxi-1 # kitne parts banenge 
        partlength=n-(noofmaxi-1) # har ek part me kitni space khali hai
        totalemptySpace=partcount * partlength  # total kitni space khali hai
        eleRemaining=len(tasks)-maxi*noofmaxi # kitne elements bache hai jo abhi insert nhi kiye gye
        totalidles=max(0,totalemptySpace - eleRemaining) # saare elements bharne ke baad kitni jgha bach gyi 
        return totalidles + len(tasks) # kahli space bachi hue + total elements
        
        
            
        
        