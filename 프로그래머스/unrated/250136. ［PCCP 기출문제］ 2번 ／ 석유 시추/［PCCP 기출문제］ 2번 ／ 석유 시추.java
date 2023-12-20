import java.util.*;
class Solution {
    static int dx[] = {-1,1,0,0}, dy[] = {0,0,-1,1};
    static int board[][], gland[][];
    static ArrayList<Integer> data;
    static boolean visited[][];
    static int N,M;
    public int solution(int[][] land) {
        int answer = 0;
        N = land.length;
        M = land[0].length;
        board = new int[N][M];
        visited = new boolean[N][M];
        data = new ArrayList<>();
        gland = land;
        
        for(int i =0; i<N; i++){
            for(int j=0; j<M; j++){
                if(gland[i][j] == 1 && !visited[i][j]){
                    BFS(i,j);
                }
            }
        }
        //탐색
        for(int j=0; j<M; j++){
            Set<Integer> set = new HashSet<>();
            for(int i=0; i<N; i++){
                if(board[i][j] != 0) set.add(board[i][j]);
            }
            int sum = 0;
            for(int index : set){
                sum += data.get(index-1);
            }
            answer = Math.max(sum, answer);
        }
        // for(int i =0; i<N; i++){
        //     System.out.println(Arrays.toString(board[i]));
        // }
        // System.out.println(data);
        return answer;
    }
    static void BFS(int x, int y){
        int number = data.size()+1;
        int count = 0;
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int [] {x,y});
        visited[x][y] = true;
        while(!q.isEmpty()){
            int []cur = q.poll();
            x = cur[0];
            y = cur[1];
            count++;
            board[x][y] = number;
            for(int i =0; i<4; i++){
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if(0 > nx || nx >= N || 0 > ny || ny >= M) continue;
                if(gland[nx][ny] == 1 && !visited[nx][ny]){
                    visited[nx][ny] = true;
                    q.add(new int[] {nx,ny});
                }
            }
        }
        data.add(count);
    }
}