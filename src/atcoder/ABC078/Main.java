import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char x =sc.next().toCharArray()[0];
        char y = sc.next().toCharArray()[0];
        if (x>y) System.out.println(">");
        if (x<y) System.out.println("<");
        if (x==y) System.out.println("=");
    }
}