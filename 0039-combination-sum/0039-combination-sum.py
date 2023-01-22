class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        self.dfs(nums,target,[],res)
        return res
    
    def dfs(self,nums,target,path,res):
        if target<0:
            return #backtracking
        if target==0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:],target-nums[i],path+[nums[i]],res)