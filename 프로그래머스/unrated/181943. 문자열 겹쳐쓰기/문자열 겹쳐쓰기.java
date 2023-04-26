class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        answer += my_string.substring(0,s) + overwrite_string;
        if(answer.length() < my_string.length()){
            int end = answer.length();
            answer += my_string.substring(end);
        }
        return answer;
    }
}