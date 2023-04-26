import java.util.*;
import java.awt.Point;
class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int answer = 0;
        int[][] moves = {{1,0}, {-1,0},{0,-1},{0, 1}};
        boolean[][] visited = new boolean[n][m];
        Queue<Point> q = new LinkedList<Point>();
        Queue<Integer> ans = new LinkedList<Integer>();
        q.add(new Point(0,0));
        ans.add(1);
        visited[0][0] = true;
        while(!q.isEmpty()){
            Point cur = q.poll();
            int count = ans.poll();
            int x = (int)cur.getX();
            int y = (int)cur.getY();
            if(x == n - 1 && y == m - 1){
                return count;
            }
            for(int i = 0 ; i<4; i++){
                int next_x = x + moves[i][0];
                int next_y = y + moves[i][1];
                if(0 <= next_x && next_x < n && 0<= next_y && next_y < m){
                    if(visited[next_x][next_y] == false && maps[next_x][next_y] == 1){
                        visited[next_x][next_y] = true;
                        q.add(new Point(next_x,next_y));
                        ans.add(count+1);
                    }
                }
            }
        }
        return -1;
    }
}