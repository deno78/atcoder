import java.util.*;

public class Main_ABC151_a {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String abc="abcdefghijklmnopqrstuvwxyz";
        String c=sc.next();
        int idx=abc.indexOf(c);
        System.out.println(abc.substring(idx+1,idx+2));
    }
}