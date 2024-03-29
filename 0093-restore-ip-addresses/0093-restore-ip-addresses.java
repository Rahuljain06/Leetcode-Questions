class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res=new ArrayList<>();
        dfs(s,0,"",res);
        return res;
    }
    private void dfs(String s, int dots, String path,List<String> res){
        if (dots==4){
            if (s.length()==0)
                res.add(path.substring(0,path.length()-1));
        return;
        }
        
        for(int i=1;i<4;i++){
            if (i>s.length())
                break;
            if (i>1 && s.charAt(0)=='0')
                continue;
            if (i>2 && Integer.parseInt(s.substring(0,i))>255)
                continue;
            dfs(s.substring(i,s.length()),dots+1,path+s.substring(0,i)+".",res);
        }
    }
}