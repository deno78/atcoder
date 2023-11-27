import java.util.*;

public class Main {
    public static void main(String[] args){
        int n=new Scanner(System.in).nextInt();
        System.out.println(
            //Integer.toString(n).contains("3") || n%3==0
            n%3==0
            ?"YES":"NO");
    }
    
}
