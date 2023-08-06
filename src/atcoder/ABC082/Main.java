import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float a=sc.nextFloat();
        float b=sc.nextFloat();
        System.out.println(
            (int) Math.ceil((a+b)/2)
        );
    }
}