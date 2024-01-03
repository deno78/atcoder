import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(
            a<10&&a>0&&b<10&&b>0?a*b:-1
        );
    }
}