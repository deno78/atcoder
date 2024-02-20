import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        double n = sc.nextDouble();
        double x = sc.nextDouble();
        double t = sc.nextDouble();
        System.out.printf("%d",
            Math.round(Math.ceil(n/x)*t)
        );
    }
}