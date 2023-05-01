import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        ArrayList<Integer> numbers = new ArrayList<>();
        for(int i = 0; i < queries.length; i++){
            ArrayList<Integer> tmp = new ArrayList<Integer>();
            int left = queries[i][0];
            int right = queries[i][1];
            int k = queries[i][2];
            for(int j = left; j <= right; j++){
                if(arr[j] > k){
                    tmp.add(arr[j]);
                }
            }
            if(tmp.isEmpty()){
                tmp.add(-1);
            }
            int min = 1000000;
            for(int element : tmp){
                if(element < min){
                    min = element;
                }
            }
            numbers.add(min);
        }
        int[] answer = new int[numbers.size()];
        for(int i = 0; i<numbers.size(); i++){
            answer[i] = numbers.get(i);
        }
        return answer;
    }
}