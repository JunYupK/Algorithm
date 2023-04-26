class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        int n = str1.length();
        for(int i = 0; i <n*2; i++){
            if(i%2 == 0 ){
                answer += String.valueOf(str1.charAt((int)i/2));
            }
            else{
                answer += String.valueOf(str2.charAt((int)i/2));
            }
        }
        return answer;
    }
}