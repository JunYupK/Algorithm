import java.util.*;
import java.io.*;

public class Main{
    static int[][] req = new int[10][10];
    static int min = -1;

    // 색종이 사이즈를 인덱스, 인덱스 별 색종이 수 세팅
    static int[] squareCnt = {0,5,5,5,5,5};

    static boolean isSquare(int y, int x, int s){
        for(int i=0;i<s;i++){
            for(int j=0;j<s;j++){
                if(req[y+i][x+j]==0) return false;
            }
        }
        return true;
    }

    static void checkSquare(int y, int x, int s, int useSquare){
        if(useSquare==1) squareCnt[s]++;
        else squareCnt[s]--;

        for(int i=0;i<s;i++){
            for(int j=0;j<s;j++){
                req[y+i][x+j] = useSquare;
            }
        }
    }

    static void backtracking(int y, int x, int cnt){
        // 가로 방향 끝까지 돌았으면 한 칸 밑으로 다시 탐색
        if(x>9){
            backtracking(y+1,0,cnt);
            return;
        }

        // 세로 방향 끝까지 돌았으면 가장 최소의 값이 정답이 되도록 출력
        // 이 때 기본값은 -1 : 색종이를 모두 덮을 수 없는 경우
        if(y>9){
            if(min == -1) min = cnt;
            else if(min > cnt) min = cnt;
            return;
        }

        // 현재 위치에 색종이를 놓을 수 없으면 가로 방향으로 한 칸 가기
        if(req[y][x] == 0) {
            backtracking(y,x+1,cnt);
            return;
        }

        // 현재 보유 색종이 수만큼 반복문 돌기
        // 이 때 큰 색종이부터 덮는 것이 색종이를 가장 최소로 사용할 수 있는 방법
        for(int s=5;s>=1;s--){

            // 현재 보유 색종이가 없지 않거나 판 내부에 존재 시 실행
            // 이 때 y+s, x+s 값은 색종이 덮은 이후의 좌표값
            // 따라서 범위 설정 시 10까지는 허용
            if(squareCnt[s] != 0 && y+s<=10 && x+s<=10){

                // 만약 현재 덮을 수 있는 색종이 크기만큼 덮을 수 있다면
                if(isSquare(y,x,s)){

                    // 색종이를 덮음
                    checkSquare(y,x,s,0);

                    // 색종이 덮은 다음으로 진행
                    backtracking(y,x+s,cnt+1);

                    // 색종이 풀고 다른 경우의 수 진행
                    checkSquare(y,x,s,1);
                }
            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int i=0;i<10;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            for(int j=0;j<10;j++){
                req[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backtracking(0,0,0);
        System.out.println(min);
    }

}