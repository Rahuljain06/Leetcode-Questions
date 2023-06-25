class Solution(object):

    def combinationSum3(self, k, target):
        res=[]
        self.dfs(range(1,10),[],target,k,res)
        return res
    
    def dfs(self,nums,path,target,k,res):
        if k<0 or target<0: 
            return #backtracking isme ham add kar rhe hain path main or jab sum bada ho jaa rha ta backtrack kar rhe hai or k ki value 0 se choti ho rhi hai to matlab elements path mai k se jyada ho rhe hai to backtrack karenge       
        if target==0 and k==0:
            res.append(path)
            return
        for i in range(len(nums)):
            # if target<nums[i]:#ham isme value add hi nahi kar rhe, path me jo target se badi ho
                # continue
            self.dfs(nums[i+1:],path+[nums[i]],target-nums[i],k-1,res)

        
            