import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int l1=sc.nextInt();
        int l2=sc.nextInt();
        int l3=sc.nextInt();
        System.out.println(l1==l2?l3:l1==l3?l2:l1);
    }
}