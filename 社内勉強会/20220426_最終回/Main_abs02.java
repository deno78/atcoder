import java.util.*;

public class Main_abs02{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = Integer.valueOf(sc.next());
        int b = Integer.valueOf(sc.next());
        if(a*b%2==0){
        System.out.println("Even");
        }else{
        System.out.println("Odd");
        }
    }
}