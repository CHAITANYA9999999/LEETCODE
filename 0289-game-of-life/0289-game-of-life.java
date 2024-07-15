class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                int nei = countNeighbours(board,i,j,m,n);

                if(board[i][j] == 0){
                    if(nei==3){
                        board[i][j] = 2;
                    }
                }else{
                    if(nei==3 || nei==2){
                        board[i][j] = 3;
                    }
                }
            }
        }
        
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(board[i][j] == 1) board[i][j] = 0;
                else if(board[i][j] == 2 || board[i][j] == 3) board[i][j] = 1;
            }
        }
    }

    public int countNeighbours(int[][] board,int r, int c, int m, int n){
        int nei=0;
        for(int i=r-1;i<r+2;i++){
            for(int j=c-1; j<c+2; j++){
                if((i==r && j==c) || i<0 || i>=m || j<0 || j>=n) continue;
                if(board[i][j] == 1 || board[i][j] == 3) nei++;
            }
        }
        return nei;
    }
}