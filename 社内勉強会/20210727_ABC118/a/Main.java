import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a=Integer.valueOf(sc.next());
        int b=Integer.valueOf(sc.next());
        System.out.println(b%a==0?a+b:b-a);
    }
}