import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        int a=0;
        for(int i=0;i<4;i++){
            a+=s.charAt(i)=='+'?1:-1;
        }
        System.out.println(a);
    }
}