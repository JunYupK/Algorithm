import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int init = n;
        int count = 0;
        while(true){
            if(n == 0){
                count += 1;
                break;
            }
            int left = n % 10;
            int right = (n % 10) + ((n/10) % 10);
            n = (left * 10) + (right % 10);
            count += 1;
            if(init == n)break;
        }
        System.out.println(count);
    }

}
