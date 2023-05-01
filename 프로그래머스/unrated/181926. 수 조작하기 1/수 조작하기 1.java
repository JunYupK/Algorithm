import java.util.*;
class Solution {
    public int solution(int n, String control) {
        int answer = n;
        int count = control.length();
        HashMap<String, Integer> check = new HashMap<String, Integer>(){{
            put("w",1);
            put("s", -1);
            put("d", 10);
            put("a",-10);
        }};
        for(int i = 0 ; i<count; i++){
            answer += check.get(String.valueOf(control.charAt(i)));
        }
        return answer;
    }
}