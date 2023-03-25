import java.util.*;
public class Main_ABC159_a{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        int m=Integer.valueOf(sc.next());
        System.out.println(n*(n-1)/2 + m*(m-1)/2);
    }
}