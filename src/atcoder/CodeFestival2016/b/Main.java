import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        String s2 = "CODEFESTIVAL2016";
        int ans = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)!=s2.charAt(i)){
                ans++;
            }
        }
        System.out.println(ans);
    }
}