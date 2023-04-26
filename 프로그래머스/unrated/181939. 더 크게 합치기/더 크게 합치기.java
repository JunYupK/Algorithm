class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String strA = String.valueOf(a);
        String strB = String.valueOf(b);
        int num1 = Integer.parseInt(strA + strB);
        int num2 = Integer.parseInt(strB + strA);
        if(num1 > num2){
            answer = num1;
        }
        else{
            answer = num2;
        }
        return answer;
    }
}