import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int a= sc.nextInt();
        int b = sc.nextInt();
        x-=a;
        x-=b*((int) x/b);
        System.out.println(x);

    }
}