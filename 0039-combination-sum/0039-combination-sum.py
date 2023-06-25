class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        self.dfs(nums,target,[],res)
        return res
    
    def dfs(self,nums,target,path,res):
        if target<0:
            return #backtracking isme ham add kar rhe hain path main or jab sum bada ho jaa rha ta backtrack kar rhe hai
        if target==0:
            res.append(path)
            return
        for i in range(len(nums)):
            # if target<nums[i]: ham isme value add hi nahi kar rhe, path me jo target se badi ho
            #     continue 
            self.dfs(nums[i:],target-nums[i],path+[nums[i]],res)