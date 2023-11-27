import java.io.*;
import java.util.*;

class Main {
    static int N, M, arr[];
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr= new int[M];
        int flag = 1;
        int sum =0;
        for (int i = 0; i < M; i++) {
            sum += flag;
            arr[i] = flag++;
        }

        if(sum > N) System.out.println(-1);
        else if(sum == N) System.out.println(arr[M-1] - arr[0]);
        else {
            int remain = N-sum;
            int index = M-1;
            while(remain != 0){
                if(index == -1) index = M-1;
                arr[index--]++;
                remain--;

            }
            System.out.println(arr[M-1] - arr[0]);
        }
    }
}