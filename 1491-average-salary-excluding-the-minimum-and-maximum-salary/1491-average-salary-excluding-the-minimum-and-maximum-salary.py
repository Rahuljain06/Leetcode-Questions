class Solution:
    def average(self, salary: List[int]) -> float:
        avg=0
        maxi=0
        mini=float('inf')
        for i in salary:
            maxi=max(maxi,i)
            mini=min(mini,i)
            avg+=i
        return (avg-mini-maxi)/(len(salary)-2) 
            