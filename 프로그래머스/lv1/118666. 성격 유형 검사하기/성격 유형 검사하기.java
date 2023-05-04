import java.util.*;
import java.lang.*;
class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        Map<Integer, Integer> map = new LinkedHashMap<Integer,Integer>();
        Map<String, Integer> dict = new LinkedHashMap<String, Integer>();
        map.put(1, 0);
        map.put(2, 0);
        map.put(3, 0);
        map.put(4, 0);
        dict.put("R", -1);
        dict.put("T", 1);
        dict.put("C", -2);
        dict.put("F", 2);
        dict.put("J", -3);
        dict.put("M", 3);
        dict.put("A", -4);
        dict.put("N", 4);
        for(int i = 0; i < survey.length; i++){
            String[] tmp = survey[i].split("");
            String flag;
            if(choices[i] >= 5){
                flag = tmp[1];
            }
            else{
                flag = tmp[0];
            }
            int score = Math.abs(4 - choices[i]);
            if(dict.get(flag) < 0){
                score = -score;
            }
            int flag2 = Math.abs(dict.get(flag));
            int num = map.get(flag2) + score;
            map.put(flag2, num);
            
        }
        System.out.println(map);
        if(map.get(1) <= 0){
            answer += "R";
        }
        else{
            answer += "T";
        }
        if(map.get(2) <= 0){
            answer += "C";
        }
        else{
            answer += "F";
        }
        if(map.get(3) <= 0){
            answer += "J";
        }
        else{
            answer += "M";
        }
        if(map.get(4) <= 0){
            answer += "A";
        }
        else{
            answer += "N";
        }
        return answer;
    }
}