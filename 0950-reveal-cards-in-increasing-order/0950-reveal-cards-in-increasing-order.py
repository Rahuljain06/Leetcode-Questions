class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        #[17,13,11,7,5,3,2]
        
        q=deque()
        for x in sorted(deck)[::-1]:
            q.rotate()
            q.appendleft(x)
            
        return list(q)
        