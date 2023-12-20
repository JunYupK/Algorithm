class Solution {
    static int dh[] = {0,1,-1,0}, dw[] = {1,0,0,-1};
    static int N;
    static int count;
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        N = board.length;
        for(int i=0; i<4; i++){
            int h_check = h + dh[i];
            int w_check = w + dw[i];
            if(0<= h_check && h_check < N && 0 <= w_check && w_check <N){
                if(board[h][w].equals(board[h_check][w_check])) count++;
            }
        }
        return count;
    }
}