import java.util.*;
import java.io.*;
//기호의 순서는 바뀌면 안된다
//최대가 음수일수도 있다는 점
class Main{
    static int N,M,ans, dx[] = {-1,1,0,0}, dy[] ={0,0,-1,1};
    static char [][] board;
    static boolean visited[][], check[] = new boolean[26];
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st  = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];
        visited = new boolean[N][M];
        for(int i=0; i<N; i++){
            String input = br.readLine();
            for(int j=0; j<M; j++){
                board[i][j] = input.charAt(j);
            }
        }
//        for(int i=0; i<N; i++) System.out.println(Arrays.toString(board[i]));
//        System.out.println('A' - 65);
        dfs(0,0,1);
        System.out.println(ans);
    }
    static void dfs(int x, int y, int count){
        ans = Math.max(count,ans);
        visited[x][y] = true;
        check[board[x][y] - 65] = true;
//        System.out.println(x + " : " + y);
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0<=nx && nx<N && 0<=ny && ny<M && !visited[nx][ny]){
                if(check[board[nx][ny] - 65]) continue;
                check[board[nx][ny] - 65] = true;
                visited[nx][ny] = true;
                dfs(nx,ny, count+1);
                check[board[nx][ny] - 65] = false;
                visited[nx][ny] = false;

            }
        }
    }
}