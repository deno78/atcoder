import java.util.*;

public class Main {
    public static void main(String[] args){
        int r = new Scanner(System.in).nextInt();
        System.out.println(r<1200?"ABC":(r<2800?"ARC":"AGC"));
    }
}
