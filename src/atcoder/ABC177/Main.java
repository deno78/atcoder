import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int d = sc.nextInt();
        int t = sc.nextInt();
        int s = sc.nextInt();
        System.out.println(
            (d<=t*s)?"Yes":"No"
        );
    }
}