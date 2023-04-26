class Solution {
    public String solution(String code) {
        String answer = "";
        String mode = "0";
        for(int i = 0; i < code.length(); i++){
            String tmp = String.valueOf(code.charAt(i));
            if(mode.equals("0")){
                if(tmp.equals("1")){
                    mode = "1";
                    continue;
                }
                else if(i % 2 == 0){
                    answer += tmp;
                }
            }
            else if(mode.equals("1")){
                if(tmp.equals("1")){
                    mode = "0";
                    continue;
                }
                else if(i % 2 != 0){
                    answer += tmp;
                }
            }

        }
        if(answer.length() == 0){
            return "EMPTY";
        }
        return answer;
    }
}