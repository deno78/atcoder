import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = Integer.valueOf(sc.next());
        int b = Integer.valueOf(sc.next());
        int c = Integer.valueOf(sc.next());
        System.out.println(a^b^c);
    }
}