import java.util.*;

public class Main {
    public static void main(String[] args){
        int k = new Scanner(System.in).nextInt();
        if(k%2==0){
            System.out.println(k*k/4);
        }else{
            System.out.println((k-k%2)*k/4);
        }
    }
}
