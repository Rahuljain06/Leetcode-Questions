class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    
    # 1:isme hamne pehle ye check kar liya ki k ya k se kam elements lekar kitne subarray banengei
    # 2: fir hamne usme se k-1 ya usse kam ki kitni array banengi
    # 3: fir last me [1-2] k-(k-1) ko subtract kar diya to sirf k elements ki subarray bachi jo hame chaiye
    
    # for eg [1,2,1,2,3] k=2
    # k=2 ya usse kam ki 12 banegi:{[1],[2],[1,2],[1,2,1],[2,1],[1],[1,2,1,2],[2,1,2],[1,2],[2],[2,3],[3]}
    # k=1 ya usse kam ki 5 banegi : {[1],[2],[1],[2],[3]}
    # k=2 ki kitni array bani = 12-5=7 
        def subarrayWithAtMostK(nums,k):
            l=0
            res=0
            d=defaultdict(int)
            for r in range(len(nums)):
                d[nums[r]]+=1
                while len(d)>k:
                    d[nums[l]]-=1
                    if not d[nums[l]]:
                        del d[nums[l]]
                    l+=1
                res+=r-l+1
            return res
        
        return subarrayWithAtMostK(nums,k) - subarrayWithAtMostK(nums,k-1)

