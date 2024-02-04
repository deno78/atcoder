import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        for(int i=1;i<=1000;i++){
            if(i%k==0&&a<=i&&i<=b){
                System.out.println("OK");
                System.exit(0);
            }
        }
        System.out.println("NG");
    }
    
}
