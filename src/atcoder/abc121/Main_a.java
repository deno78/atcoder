import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] a = new int[]{sc.nextInt(),sc.nextInt(),sc.nextInt(),sc.nextInt()};
        System.out.println((a[0]-a[2])*(a[1]-a[3]));
    }
}