class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        self.dfs(nums,target,[],res)
        return res
        
    def dfs(self,nums,target,path,res):
        if target==0:
            res.append(path)
            return

        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            if nums[i]>target:
                break
            self.dfs(nums[i+1:],target-nums[i],path+[nums[i]],res)