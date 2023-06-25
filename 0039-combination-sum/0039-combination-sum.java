class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res= new ArrayList<>();
        dfs(nums,new ArrayList<>(),target, res);
        return res;
    }
    
    public void dfs(int[] nums,List<Integer> path,int target,List<List<Integer>> res){
        if (target == 0){
            res.add(path);
            return;
        }
        for (int i=0;i<nums.length;i++){
            if (nums[i]>target)
                continue;
            List<Integer> c = new ArrayList<>(path);
            c.add(nums[i]);
            dfs(Arrays.copyOfRange(nums,i,nums.length), c, target-nums[i],res);
        }
    }
}