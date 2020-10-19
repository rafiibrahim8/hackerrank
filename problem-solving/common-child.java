// https://www.hackerrank.com/challenges/common-child/problem

import java.util.Scanner;

public class Solution {
    private static int commonChild(String a,String b){
        int[][] table = new int[a.length()+1][b.length()+1];
        for(int i=0;i<a.length();i++){
            for(int j=0;j<b.length();j++){
                if(a.charAt(i) == b.charAt(j))
                    table[i+1][j+1]=table[i][j]+1;
                else
                    table[i+1][j+1]=Math.max(table[i+1][j],table[i][j+1]);
            }
        }
        return table[a.length()][b.length()];
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.nextLine();
        String s2 = scanner.nextLine();

        System.out.println(commonChild(s1, s2));
    }
    
}
