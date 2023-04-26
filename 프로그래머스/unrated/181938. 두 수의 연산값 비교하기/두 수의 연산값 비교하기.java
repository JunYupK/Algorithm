class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String strA = String.valueOf(a);
        String strB = String.valueOf(b);
        int numA = Integer.valueOf(strA + strB);
        int numB = 2 * a * b;
        if(numA > numB){
            return numA;
        }
        else{
            return numB;
        }
    }
}