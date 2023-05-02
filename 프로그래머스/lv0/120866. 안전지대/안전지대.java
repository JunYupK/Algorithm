import java.util.*;

class Solution {
    static class Pos{
    int r, c, cost;
    public Pos(int r, int c, int cost){
        this.r = r;
        this.c = c;
        this.cost = cost;
        }
    }
    public int solution(int[][] board) {
        int answer = 0;
        int n = board.length;
        int m = board[0].length;
        Queue<Pos> q = new LinkedList<>();
        int[][] moves = {{-1,-1}, {-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        for(int i = 0; i < n ; i++){
            for(int j = 0; j < m; j++){
                if(board[i][j] == 1){
                    q.add(new Pos(i,j,0));
                }
            }
        }
        while(!q.isEmpty()){
            Pos cur = q.poll();
            for(int i = 0; i<8; i++){
                int dx = moves[i][0];
                int dy = moves[i][1];
                int next_x = cur.r + dx;
                int next_y = cur.c + dy;
                if(0 <= next_x && next_x < n && 0<=next_y && next_y < m){
                    if(board[next_x][next_y] == 0){
                        board[next_x][next_y] = 2;
                    }
                }
            }
        }
        for(int i = 0; i < n ; i++){
            for(int j = 0; j<m; j++){
                if(board[i][j] == 0){
                    answer += 1;
                }
            }
        }
        return answer;
    }
}