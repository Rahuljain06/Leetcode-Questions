class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # 46 permutation jaisa hai 
        res=set()
        self.dfs(tiles, "",res)
        return len(res)-1 #empty string add hogi ek extra esiliye -1 kiya
    def dfs(self,nums,path,res):
        res.add(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+nums[i],res)