class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Approach: ham basically pehle max frequency wala element nikal lenge elements me se hame diye gye haior ye bhi ho sakta hai ki maximum frequency ke multiple elements ho to ham kitne elements hai maximum frequency wale vo bhi count kar lenge. fir ham place karna shuru karennge gaps me according to n for eg: tasks = ["A","A","A","B","B","B","C"], n = 2 me jo max frequency aayegi vo 3 aayegi and no of maximum frequency elements 2 aayenge A,B to follow these steps:
# 1: pehle ham A ko place karenge n gaps par like: A X X A X X A
# 2: aise hi ham saare maximum frequency wale elements place karne hai to ham B ko place karenge A ke baad 
# A B X A B X A B 
# 3: iske baad ham Total Empty Space nikal lenge to usko nikalne ke liye: total kitne part banenge [maxiumfrequency-1] * har ek part me kitni khali space hai [n-(no.of maximum frequency elements -1)] i.e 
#[3-1]*[2-(2-1)] => 2 * 1 => 2
# 4: fir ham nikalenge kitne elements reh gye hai jo abhi tak place nhi hue hai to ham total elemnts me se - maximumfrequency wale elements minus kar denge => len(elements)- maxifrequency * no of maxifrequency elements
# remaining elements => 7-3*2 =>1
# A B C A B X A B 
# 5: fir ham Idle space nikal lenge jo saare elements place karne ke baad khali bachi=> max(0,total empty Space - remaining elements jo place nhi hue) => max(0,2-1) =>1 
# fir last me ham total elements + Idle Space return kar denge
# 7 + 1 =>  8
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
        emptySpaceEachPart=n-(noofmaxi-1) # har ek part me kitni space khali hai
        totalemptySpace=partcount * emptySpaceEachPart  # total kitni space khali hai
        eleRemaining=len(tasks)-maxi*noofmaxi # kitne elements bache hai jo abhi insert nhi kiye gye
        totalidles=max(0,totalemptySpace - eleRemaining) # saare elements bharne ke baad kitni jgha bach gyi 
        return totalidles + len(tasks) # kahli space bachi hue + total elements
        
        
            
        
        