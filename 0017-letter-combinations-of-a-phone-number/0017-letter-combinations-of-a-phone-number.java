class Solution {
    public List<String> letterCombinations(String digits) {
        Map<String,String> d = new HashMap<>();
        d.put("2","abc");
        d.put("3","def");
        d.put("4","ghi");
        d.put("5","jkl");
        d.put("6","mno");
        d.put("7","pqrs");
        d.put("8","tuv");
        d.put("9","wxyz");
                
        List<String> res=new ArrayList<>();
        
        if (digits.length()==0)
            return res;
        
        dfs(digits,"",0,d,res);
        return res;
    }
    private void dfs(String nums,String path,Integer index, Map<String,String> d,List<String> res){
        if(nums.length()==index){
            res.add(path);
            return;
        }
        String s=d.get(Character.toString(nums.charAt(index)));
        for (int i=0;i<s.length();i++){
            dfs(nums,path+s.charAt(i),index+1,d,res);
        }
            
    }
}