import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int n=sc.nextInt();
        while(true){
            if(n%a==0&&n%b==0){
                System.out.println(n);
                System.exit(0);
            }
            n++;
        }
    }
    
}
