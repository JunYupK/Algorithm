class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        int n = queries.length;
        for(int i = 0; i<n; i++){
            int left = queries[i][0];
            int right = queries[i][1];
            int tmp;
            tmp = arr[left];
            arr[left] = arr[right];
            arr[right] = tmp;
        }
        return arr;
    }
}