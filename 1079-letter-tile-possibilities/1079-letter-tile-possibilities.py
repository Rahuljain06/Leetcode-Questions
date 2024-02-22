class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # 46 permutation jaisa hai 
        res=set()
        self.dfs(tiles, "",res)
        return len(res)
    def dfs(self,nums,path,res):
        if path: # ye hamne seif empty string add na ho esiliye lagayi hai
            res.add(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+nums[i],res)