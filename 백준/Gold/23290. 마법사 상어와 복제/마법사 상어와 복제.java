import java.io.*;
import java.util.*;

public class Main {
    static int M, S,shark_x, shark_y;
    static int dx[] = {-1,0,1,0}, dy[] = {0,-1,0,1}, check[];
    static int fdx[] = {0,0,-1,-1,-1,0,1,1,1}, fdy[] = {0,-1,-1,0,1,1,1,0,-1};
    static ArrayList<Integer> [][]board, copyWaitList;
    static int [][]visited;
    static int max, ans;
    static int maxIndex[];
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        board = new ArrayList[4][4];
        visited = new int[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                board[i][j] = new ArrayList<>();
            }
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int dir = Integer.parseInt(st.nextToken());
            board[x-1][y-1].add(dir);
        }
        st = new StringTokenizer(br.readLine());
        shark_x = Integer.parseInt(st.nextToken())-1;
        shark_y = Integer.parseInt(st.nextToken())-1;
        for (int i = 0; i < S; i++) {
            copyWait();
            moveCheck();
//            printBoard();
            check = new int[3];
            moveShark();
            checkTrace();
            copyResult();
//            printBoard();
//            for (int j = 0; j < 4; j++) {
//                System.out.println(Arrays.toString(visited[j]));
//            }
//            System.out.println();
        }
        result();
        System.out.println(ans);

    }
    static void printBoard(){
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                System.out.print("[");
                for (int x:board[i][j]) System.out.print(x+",");
                System.out.print("]");
            }
            System.out.println();
        }
        System.out.println();
    }
    static void copyWait(){
        copyWaitList = new ArrayList[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                copyWaitList[i][j] = new ArrayList<>();
                for(int x : board[i][j]) copyWaitList[i][j].add(x);
            }
        }
    }
    static void copyResult(){
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                for(int x:copyWaitList[i][j]) board[i][j].add(x);
            }
        }
    }
    static void moveCheck(){
        //copy
        ArrayList<Integer>[][]copied = new ArrayList[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                copied[i][j] = new ArrayList<>();
            }
        }
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                fish : for(int dir:board[i][j]){
//                    System.out.println("prev : "+ i + ": " + j + " " + dir);
                    for (int k = 0; k < 8; k++) {
                        if(dir == 0) dir = 8;
                        int nx = i + fdx[dir];
                        int ny = j + fdy[dir];
                        if(0<=nx && nx <4 && 0<=ny && ny<4 && visited[nx][ny] == 0){
                            if(shark_x != nx || shark_y != ny){
                                copied[nx][ny].add(dir);
                                continue fish;
                            }
                        }
                        dir--;
                    }
//                    System.out.println("after " + dir);
                    copied[i][j].add(dir);
                }
            }
        }
        board = copied;
    }
    static void moveShark(){
        max = -1;
        maxIndex = new int[3];
        perm(0);
        //이동하면서 물고기 삭제
        for(int index:maxIndex){
            int nx = shark_x + dx[index];
            int ny = shark_y + dy[index];
            if(!board[nx][ny].isEmpty()){
                board[nx][ny].clear();
                visited[nx][ny] = 3;
            }
            shark_x = nx;
            shark_y = ny;
        }
    }
    static void perm(int depth){
        if(depth == 3){
            boolean tmp[][] = new boolean[4][4];
            int count = 0;
            int x= shark_x;
            int y = shark_y;
            for(int index:check){
                int nx = x + dx[index];
                int ny = y + dy[index];
                if(nx<0 || nx>=4 || ny<0 || ny>=4) return;
                x = nx;
                y = ny;
                if(!tmp[nx][ny]){
                    count += board[nx][ny].size();
                    tmp[nx][ny] = true;
                }
            }
            if(count > max){
                max = count;
                for (int i = 0; i < 3; i++) {
                    maxIndex[i] = check[i];
                }
            }
            return;
        }
        for (int i = 0; i < 4; i++) {
            check[depth] = i;
            perm(depth+1);
        }
    }
    static void checkTrace(){
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if(visited[i][j] > 0) visited[i][j]--;
            }
        }
    }
    static void result(){
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                ans += board[i][j].size();
            }
        }
    }
}