class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res= new ArrayList<>();
        Arrays.sort(nums);
        dfs(nums,new ArrayList<>(),res);
        return res;
    }
    public void dfs(int[] nums,List<Integer> path, List<List<Integer>> res){
        res.add(path);
        for(int i=0;i<nums.length;i++){
            if (i>0 && nums[i]==nums[i-1]){
                continue;
            }
            List<Integer> c=new ArrayList<>(path);
            c.add(nums[i]);
            dfs(Arrays.copyOfRange(nums,i+1,nums.length),c,res);
        }
            
    }    
}