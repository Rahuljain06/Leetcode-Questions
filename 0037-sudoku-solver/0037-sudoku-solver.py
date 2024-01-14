class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for r in range(len(board)):
            for c in range(len(board)):
                
                if board[r][c]==".":
                    for ch in "123456789":
                        if self.isValid(r,c,ch,board):
                            board[r][c]=ch

                            if self.solveSudoku(board)==True:
                                return True
                            else:
                                board[r][c]="."
                    return False
        return True
    
    
    def isValid(self,row,col,ch,board):
        for i in range(len(board)):
            if board[row][i]==ch:
                return False
            
            if board[i][col]==ch:
                return False
            #now we will check the box contains the ch
            if (board[3*(row//3)+i//3][3*(col//3)+i%3]==ch):
                return False
        return True