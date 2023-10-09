import java.util.*;
import java.io.*;
public class Main {
    static int N,M,D,C;
    static int board[][], dx[] = {0,0,-1,-1,-1,0,1,1,1}, dy[] = {0,-1,-1,0,1,1,1,0,-1};
    static int wdx[]={-1,1,1,-1}, wdy[]={-1,-1,1,1};
    static boolean cloud[][];
    static int ans;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        cloud = new boolean[N][N];
        cloud[N-1][0] = true;
        cloud[N-1][1] = true;
        cloud[N-2][0] = true;
        cloud[N-2][1] = true;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            D = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            cloudMove();
            rainDrop();
            magicCopy();
            makeCloud();
//            print();
        }
        calWater();
//        print();
        System.out.println(ans);
    }
    static void print(){
        for (int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
        for (int j = 0; j < N; j++) {
            System.out.println(Arrays.toString(cloud[j]));
        }
        System.out.println();
    }
    static void cloudMove(){
        move();
    }
    static void move(){
        boolean copied[][] = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(cloud[i][j]){
                    //이동
                    int c = C;
                    int x = i;
                    int y = j;
                    while(c!=0){
                        int nx = x+dx[D];
                        int ny = y+dy[D];
                        if(0<=nx && nx<N && 0<=ny && ny<N){
                            x = nx;
                            y = ny;
                            c--;
                            continue;
                        }
                        else{
                            if(nx<0) nx=N-1;
                            if(ny<0) ny=N-1;
                            if(nx>=N) nx=0;
                            if(ny>=N) ny=0;
                            x = nx;
                            y = ny;
                        }
                        c--;
                    }
                    cloud[i][j] = false;
                    copied[x][y] = true;
                }
            }
        }
        cloud = copied;
    }
    static void rainDrop(){
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(cloud[i][j]) board[i][j]++;
            }
        }
    }
    static void magicCopy(){
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(cloud[i][j]){
                    int tmp = 0;
                    for (int d = 0; d < 4; d++) {
                        int nx = i+wdx[d];
                        int ny = j+wdy[d];
                        if(0<=nx && nx<N && 0<=ny && ny<N && board[nx][ny] > 0) tmp++;
                    }
                    board[i][j] += tmp;
                }
            }
        }
    }
    static void makeCloud(){
        boolean newCloud[][] = new boolean[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if(board[i][j] >= 2 && !cloud[i][j]){
                        board[i][j] -= 2;
                        newCloud[i][j] = true;
                    }
                }
            }
        cloud = newCloud;
    }
    static void calWater(){
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ans += board[i][j];
            }
        }
    }
}