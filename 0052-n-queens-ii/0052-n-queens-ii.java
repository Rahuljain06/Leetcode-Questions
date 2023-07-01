class Solution {
    int res = 0;
    public int totalNQueens(int n) {
        Set<Integer> col=new HashSet<>();
        Set<Integer> pos=new HashSet<>();
        Set<Integer> neg=new HashSet<>();
        
        char[][] board = new char[n][n]; 

        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        
        dfs(0,col,pos, neg, board,n);
        
        return res;
    }
        
    public void dfs(int r,Set<Integer> col,Set<Integer> pos,Set<Integer> neg,char[][] board, int n){
        
        if(n==r){
            res++;
            return;
        }
        
        for(int c=0;c<n;c++){
            if(col.contains(c) || pos.contains(r-c) || neg.contains(r+c))
                continue;
            col.add(c);
            pos.add(r-c);
            neg.add(r+c);
            board[r][c]='Q';
            
            dfs(r+1,col,pos, neg, board,n);
            
            col.remove(c);
            pos.remove(r-c);
            neg.remove(r+c);
            board[r][c]='.';
        }
        
    }
    
}