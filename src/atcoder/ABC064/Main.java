import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println(
         Integer.valueOf(sc.next() + sc.next()+sc.next())%4==0?"YES":"NO"
        );
    }
}