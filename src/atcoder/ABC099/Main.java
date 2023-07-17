import java.util.*;

public class Main{
    public static void main(String[] args){
        int n = new Scanner(System.in).nextInt();
        String s = "CDEFGHIJKLMNOPQRSTUVWXYZ";
        System.out.println("AB" +  s.charAt((int)(n-1)/999));
    }
}