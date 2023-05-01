import java.util.*;
class Solution {
    public String solution(int[] numLog) {
        int n = numLog.length;
        String answer = "";
        HashMap<Integer, String> check = new HashMap<Integer, String>(){{
            put(1, "w");
            put(-1, "s");
            put(10, "d");
            put(-10, "a");
        }};
        for(int i = 1; i < n ; i ++){
            answer += check.get(numLog[i] - numLog[i-1]);
        }
        return answer;
    }
}