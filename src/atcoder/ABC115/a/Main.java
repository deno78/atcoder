import java.util.*;

public class Main {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String ans="Christmas";
        int d=sc.nextInt();
        for(int i=0;i<25-d;i++){
            ans+=" Eve";
        }
        System.out.println(ans);
    }
    
}
