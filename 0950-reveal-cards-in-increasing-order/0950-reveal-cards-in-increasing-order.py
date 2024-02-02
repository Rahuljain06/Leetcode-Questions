class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
# Let's walk through the example:
# Input: [17,13,11,2,3,5,7]
# Output: [2,13,3,11,5,17,7]

# Sort the deck: [2,3,5,7,11,13,17], this is the increasing order we want to generate
# Initialize the queue: [0,1,2,3,4,5,6], this is the index of the result array
# The first card we pick is res[0], observe the deck, it should be deck[0]==2, so assign res[0]=2
# Then we put res[1] to the bottom, so we re-insert 1 to the queue
# The second card we pick is res[2], which should be deck[1]==3, so assign res[2]=3
# Then we re-insert 3 to the queue
# Each time we assign 1 value to the res, so we repeat this n times.
        deck.sort()
        q=deque()
        for i in range(len(deck)):
            q.append(i)
        res=[0]*len(deck)
        for i in range(len(deck)):
            res[q.popleft()]=deck[i]
            if q:
                q.append(q.popleft())
        return res
            
            
            
        