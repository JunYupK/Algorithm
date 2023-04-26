import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String answer = "";
        for(int i = 0 ; i< a.length(); i++){
            if(Character.isUpperCase(a.charAt(i))){
                answer += String.valueOf(a.charAt(i)).toLowerCase();
            }
            else{
                answer += String.valueOf(a.charAt(i)).toUpperCase();
            }
        }
        
        System.out.println(answer);
    }
}