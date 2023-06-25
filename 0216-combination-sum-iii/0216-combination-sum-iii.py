class Solution(object):

    def combinationSum3(self, k, target):
        res=[]
        self.dfs(range(1,10),[],target,k,res)
        return res
    
    def dfs(self,nums,path,target,k,res):
        if k<0 or target<0:
            return
        if k==0 and target!=0:
            return
        if k>0 and target==0:
            return
        
        if target==0 and k==0:
            res.append(path)
            return
        for i in range(len(nums)):
            if target<nums[i]:
                continue
            self.dfs(nums[i+1:],path+[nums[i]],target-nums[i],k-1,res)

        
            