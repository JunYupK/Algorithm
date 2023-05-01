class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int count = 1;
        int x = 0;
        int y = n-1;
        while(count < n * n){
            for(int i = x; i <= y; i++){
                answer[x][i] = count;
                count += 1;
            }
            for(int i = x + 1; i <=y; i ++){
                answer[i][y] = count;
                count += 1;
            }
            for(int i = y-1; i >= x; i--){
                answer[y][i] = count;
                count += 1;
            }
            for(int i = y-1; i > x; i--){
                answer[i][x] = count;
                count += 1;
            }
            x += 1;
            y -= 1;
        }
        if(n % 2 != 0){
            answer[x][y] = count;
        }
        return answer;
    }
}