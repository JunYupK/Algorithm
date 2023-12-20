import java.util.*;
class Solution {
    static int attIndex;
    static int hp;
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int end = attacks[attacks.length-1][0];
        int stric = 0;
        ArrayDeque<int[]> q = new ArrayDeque<>();
        hp = health;
        
        for(int i=0; i<attacks.length; i++){
            q.add(attacks[i]);
        }
        for(int time=0; time<=end; time++){
            if(time == q.peekFirst()[0]){
                int dmg = q.pop()[1];
                hp -= dmg;
                stric = 0;
                if(hp <= 0) return -1;
            }
            else{
                hp += bandage[1];
                stric++;
                if(stric == bandage[0]){
                    stric = 0;
                    hp += bandage[2];
                }
                if(hp >= health) hp = health;
            }
            
        }
        return hp;
    }
}