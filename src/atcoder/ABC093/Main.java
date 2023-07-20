import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        char[] cs = s.toCharArray();
        Arrays.sort(cs);
        if(String.copyValueOf(cs).equals("abc")){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}