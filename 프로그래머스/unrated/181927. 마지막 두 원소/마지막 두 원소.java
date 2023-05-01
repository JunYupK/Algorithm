class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        int n = num_list.length;
        int flag = 0;
        if(num_list[n-1] > num_list[n-2]){
            flag = num_list[n-1] - num_list[n-2];
        }
        else{
            flag = num_list[n-1] * 2;
        }
        int[] result = new int[n+1];
        for(int i =0; i < n; i++){
            result[i] = num_list[i];
        }
        result[n] = flag;
        return result;
    }
}