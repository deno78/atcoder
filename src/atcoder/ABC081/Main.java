import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        int ans=0;
        for(char c:s.toCharArray()){
            if(c=='1'){
                ans++;
            }
        }
        System.out.println(ans);
    }
}