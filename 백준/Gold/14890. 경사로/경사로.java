import java.util.*;
import java.io.*;
public class Main {
    static int n,N, L,l;
    static int board[][];
    static int ans;
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        n = N;
        L = Integer.parseInt(st.nextToken());
        l = L;
        board = new int[N][N];
        for(int i =0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        garoCheck();
        seroCheck();
        System.out.println(ans);
    }

    public static boolean calRow(int row) {
        boolean[] isIncline = new boolean[n]; //경사면 설치 여부를 확인하는 배열

        for(int i = 0; i < n - 1; i++) {
            int diff = board[row][i] - board[row][i + 1];

            if(diff > 1 || diff < -1) return false; //높이차 1 초과하므로 false
            else if(diff == -1) { // 다음 계단이 한 계단 높다
                for(int j = 0; j < l; j++) { // 올라가는 경사로를 설치할 수 있는지 확인한다.
                    if(i - j < 0 || isIncline[i - j]) return false;
                    if(board[row][i] != board[row][i - j]) return false;
                    isIncline[i - j]  = true; //경사면 설치
                }
            }
            else if(diff == 1) { //다음 계단이 한 계단 낮다
                for(int j = 1; j <= l; j++) { //내려가는 경사로를 설치할 수 있는지 확인한다.
                    if(i + j >= n || isIncline[i + j]) return false;
                    if(board[row][i] - 1 != board[row][i + j]) return false;
                    isIncline[i + j] = true; //경사면 설치
                }
            }
        }
        return true;
    }
    static void garoCheck(){
        for(int sero=0; sero<N; sero++){
            boolean check[] = new boolean[N];
            boolean isAns = true;
            garo : for(int i=0; i<N-1; i++){
                int flag = board[sero][i] - board[sero][i+1];
                if(flag > 1 || flag < -1) {
                    isAns = false;
                    break;
                }
                else if(flag == -1){
                    for(int j =0; j<L; j++){
                        if(i-j < 0 || check[i-j]) {
                            isAns = false;
                            break garo;
                        }
                        if(board[sero][i] != board[sero][i-j]) {
                            isAns = false;
                            break garo;
                        }
                        check[i-j] = true;
                    }
                }
                else if(flag == 1){
                    for(int j=1; j<=L; j++){
                        if(i+j>=N || check[i+j]) {
                            isAns = false;
                            break garo;
                        }
                        if(board[sero][i] - 1 != board[sero][i+j]) {
                            isAns = false;
                            break garo;
                        }
                        check[i+j] = true;
                    }
                }
            }
            if(isAns) ans++;
        }
    }
    static void seroCheck(){
        for(int garo=0; garo<N; garo++){
            boolean check[] = new boolean[N];
            boolean isAns = true;
            sero : for(int i=0; i<N-1; i++){
                int flag = board[i][garo] - board[i+1][garo];
                if(flag > 1 || flag < -1) {
                    isAns = false;
                    break;
                }
                else if(flag == -1){
                    for(int j=0; j<L; j++){
                        if(i-j<0 ||check[i-j]) {
                            isAns = false;
                            break sero;
                        }
                        if(board[i][garo] != board[i - j][garo]) {
                            isAns = false;
                            break sero;
                        }
                        check[i-j] = true;
                    }
                }
                else if(flag == 1){
                    for(int j=1; j<=L; j++){
                        if(i+j >= N || check[i+j]){
                            isAns = false;
                            break sero;
                        }
                        if(board[i][garo]-1 != board[i+j][garo]) {
                            isAns = false;
                            break sero;
                        }
                        check[i+j] = true;
                    }
                }
            }
            if(isAns) ans++;
        }
    }
}