class Solution {
    public int totalNQueens(int n) {
        Set<Integer> col=new HashSet<>();
        Set<Integer> pos=new HashSet<>();
        Set<Integer> neg=new HashSet<>();
        
        List<List<String>> res = new ArrayList<>();
        
        char[][] board = new char[n][n]; 

        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        
        dfs(0,col,pos, neg, board,n,res);
        
        return res.size();
    }
        
    public void dfs(int r,Set<Integer> col,Set<Integer> pos,Set<Integer> neg,char[][] board, int n, List<List<String>> res){
        
        if(n==r){
            List<String> copy = new ArrayList<>();
            for (char[] row : board) {
                copy.add(new String(row));
            }
            res.add(copy);
            return;
        }
        
        for(int c=0;c<n;c++){
            if(col.contains(c) || pos.contains(r-c) || neg.contains(r+c))
                continue;
            col.add(c);
            pos.add(r-c);
            neg.add(r+c);
            board[r][c]='Q';
            
            dfs(r+1,col,pos, neg, board,n,res);
            
            col.remove(c);
            pos.remove(r-c);
            neg.remove(r+c);
            board[r][c]='.';
        }
        
    }
    
}