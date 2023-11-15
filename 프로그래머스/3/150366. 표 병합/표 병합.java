import java.util.*;
class Solution {
    static String [][]data = new String[51][51];
    static int [][]indexs = new int[51][51];
    static ArrayList<String> answer = new ArrayList<>();
    public String[] solution(String[] commands) {
        int count = 0;
        for(int i=1; i<51; i++){
            for(int j=1; j<51; j++) indexs[i][j] = count++;
        }
        
        for(String command:commands){
            String []tmp = command.split(" ");
            switch(tmp[0]){
                case "UPDATE":
                    if(tmp.length == 4){
                        int r = Integer.parseInt(tmp[1]);
                        int c = Integer.parseInt(tmp[2]);
                        update1(r,c,tmp[3]);
                    }
                    else{
                        update2(tmp[1], tmp[2]);
                    }
                    break;
                case "MERGE":
                    merge(Integer.parseInt(tmp[1]), Integer.parseInt(tmp[2]),Integer.parseInt(tmp[3]),Integer.parseInt(tmp[4]));
                    break;
                case "UNMERGE":
                    unmerge(Integer.parseInt(tmp[1]),Integer.parseInt(tmp[2]));
                    break;
                case "PRINT":
                    print(Integer.parseInt(tmp[1]),Integer.parseInt(tmp[2]));
                    break;
                    
            }
            // for(int i=1; i<=4; i++){
            //     for(int j=1; j<=4; j++){
            //         System.out.print(indexs[i][j] + " ");
            //     }
            //     System.out.println();
            // }
            // System.out.println();
        }
        String tmp[] = new String[answer.size()];
        for(int i=0; i<answer.size(); i++) tmp[i] = answer.get(i);
        return tmp;
    }
    static void update1(int r, int c, String value){
        int flag = indexs[r][c];
        for(int i=1; i<51; i++){
            for(int j=1; j<51; j++){
                if(flag == indexs[i][j]) data[i][j] = value;
            }
        }
    }
    static void update2(String value1, String value2){
        for(int i=1; i<51; i++){
            for (int j=1; j<51; j++){
                if(data[i][j] == null) continue;
                if(data[i][j].equals(value1)) data[i][j] = value2;
            }
        }
    }
    static void merge(int r1, int c1, int r2, int c2){
        int flag1;
        int flag2;
        String value = data[r1][c1];
        if(value == null) value = data[r2][c2];
        if(indexs[r1][c1] >= indexs[r2][c2]) {
            flag1 = indexs[r2][c2];
            flag2 = indexs[r1][c1];
        }
        else{
            flag1 = indexs[r1][c1];
            flag2 = indexs[r2][c2];
        }
        for(int i=1; i<51; i++){
            for (int j=1; j<51; j++){
                if(indexs[i][j] == flag2){
                    data[i][j] = value;
                    indexs[i][j] = flag1; 
                } 
                if(indexs[i][j] == flag1){
                    data[i][j] =value;
                }
            }
        }
        
        
    }
    static void unmerge(int r, int c){
        int flag = indexs[r][c];
        String dummy = data[r][c];
        int count = 0;
        for(int i=1; i<51; i++){
            for(int j=1; j<51; j++){
                if(indexs[i][j] == flag){
                    indexs[i][j] = count;
                    data[i][j] = null;
                }
                count++;
            }
        }
        data[r][c] = dummy;
    }
    static void print(int r, int c){
        if(data[r][c] == null) answer.add("EMPTY");
        else answer.add(data[r][c]);
    }
}