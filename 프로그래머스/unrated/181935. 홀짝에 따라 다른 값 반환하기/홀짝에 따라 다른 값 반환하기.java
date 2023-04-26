class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean flag = false;
        if(n%2 == 0){
            flag = true;
        }
        for(int i = 1 ; i <=n; i++){
            if(flag == true && i % 2 == 0){
                answer += i * i;
            }
            else if(flag == false && i % 2 == 1){
                answer += i;
            }
        }
        return answer;
    }
}