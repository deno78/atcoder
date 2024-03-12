import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        System.out.println(
            (c==0&&a>b)||(c==1&&a>=b)?"Takahashi":"Aoki"
        );
    }
    
}
