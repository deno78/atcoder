import java.util.*;

public class Main_A {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(Math.max(Math.max(a*2-1,b*2-1),a+b));
    }
}
