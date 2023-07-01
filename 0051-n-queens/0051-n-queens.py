class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        neg=set()
        pos=set()
        res=[]
        board=[["."]*n for i in range(n)]
        self.backtrack(0,col,neg,pos,board,n,res)
        return res
        
    def backtrack(self,r,col,neg,pos,board,n,res):
        if r==n:
            copy=["".join(row) for row in board]
            res.append(copy)
            print(copy)
            return

        for c in range(n):
            if c in col or r+c in neg or r-c in pos:
                continue
            col.add(c)
            neg.add(r+c)
            pos.add(r-c)
            board[r][c]="Q"

            self.backtrack(r+1,col,neg,pos,board,n,res)

            col.remove(c)
            neg.remove(r+c)
            pos.remove(r-c)
            board[r][c]="."