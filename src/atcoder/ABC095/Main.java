import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        int ans=700;
        for(char c : s.toCharArray()){
            if(c=='o')ans+=100;
        }
        System.out.println(ans);
    }
}