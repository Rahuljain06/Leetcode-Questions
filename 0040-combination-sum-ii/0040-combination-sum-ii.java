class Solution {
    public List<List<Integer>> combinationSum2(int[] nums, int target) {
        List<List<Integer>> res= new ArrayList<>();
        Arrays.sort(nums);
        dfs(nums,new ArrayList<>(), target, res);
        return res;
    }
    
    public void dfs(int[] nums, List<Integer> path, int target, List<List<Integer>> res ){
        if(target==0)
            res.add(path);
        for (int i=0; i<nums.length;i++){
            if (i>0 && nums[i]==nums[i-1]){
                continue;
            }
            if (nums[i]>target)
                break;
            List<Integer> c= new ArrayList<>(path);
            c.add(nums[i]);
            dfs(Arrays.copyOfRange(nums,i+1,nums.length), c, target-nums[i],res);
        }
    }
}