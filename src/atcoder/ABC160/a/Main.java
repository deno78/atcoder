import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        System.out.println(
            s.charAt(2)==s.charAt(3)
            &&
            s.charAt(4)==s.charAt(5)
            ?"Yes":"No"
        );
    }
}