import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] query) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < arr.length; i++){
            list.add(arr[i]);
        }
        for(int i = 0 ; i<query.length; i++){
            if(i % 2 == 0){
                int n = (list.size() - 1) - query[i];
                for(int j =0; j<n; j++){
                    list.remove(list.size()-1);
                }
            }
            else{
                int n = query[i];
                for(int j = 0; j < n; j++){
                    list.remove(0);
                }
            }
        }
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}