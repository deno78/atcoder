import java.util.*;

public class Main_A{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt()-1;
        String s = sc.next();
        System.out.println(s.substring(0,k) + s.substring(k,k+1).toLowerCase() + s.substring(k+1) );
    }
}