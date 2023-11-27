import java.io.*;
import java.util.*;

class Main {
    static int N, arr[], distance[], min = Integer.MAX_VALUE;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N];
        distance = new int[N-1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N-1; i++) {
            distance[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        long cost = 0;
        for (int i = 0; i < N-1; i++) {
            min = Math.min(arr[i], min);
            cost += min * distance[i];
        }
        System.out.println(cost);
    }
}