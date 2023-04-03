class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        lo=0
        hi=len(people)-1
        while lo<=hi:
            if people[lo]+people[hi] <=limit:
                lo+=1
                hi-=1
                boats+=1
            elif people[lo]+people[hi]>limit:
                boats+=1
                hi-=1
        return boats
        