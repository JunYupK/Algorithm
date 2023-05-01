import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(int i = l; i<=r; i++){
            String[] tmp = String.valueOf(i).split("");
            boolean flag = true;
            for(String e:tmp){
                if(e.equals("5") || e.equals("0")){
                    continue;
                }
                else{
                    flag = false;
                    break;
                }
            }
            if(flag){
                result.add(i);
            }
        }
        if(result.isEmpty()){
            result.add(-1);
        }
        int[] answer = new int[result.size()];
        for(int i = 0; i < result.size(); i++){
            answer[i] = result.get(i);
        }
        return answer;
    }
}