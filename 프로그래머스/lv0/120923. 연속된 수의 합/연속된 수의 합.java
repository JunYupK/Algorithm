import java.util.*;
class Solution {
    public int[] solution(int num, int total) {
        int []answer = new int[num];
        int a = (2*total/num + 1 - num) / 2;
        for(int i = 0; i < num; i++){
            answer[i] = a+i;
        }
        return answer;
    }
}