class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] nums, List<Integer> path, List<List<Integer>> res) {
        res.add(path);
        for (int i = 0; i < nums.length; i++) {
            List<Integer> c=new ArrayList<>(path);
            c.add(nums[i]);
            dfs(Arrays.copyOfRange(nums, i + 1, nums.length),c,res);
        }
    }
}
