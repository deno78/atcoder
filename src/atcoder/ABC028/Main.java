import java.util.*;

public class Main {
    public static void main(String[] args){
        int n = new Scanner(System.in).nextInt();
        if(n<=59){
            System.out.println("Bad");
        }else if(n<=89){
            System.out.println("Good");
        }else if(n<=99){
            System.out.println("Great");
        }else{
            System.out.println("Perfect");
        }
   }
}
