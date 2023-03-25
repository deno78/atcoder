import java.util.*;
public class Main_ABC142_a{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float n=Float.valueOf(sc.next());
        if(n%2==0){
            System.out.println((n/2)/n);
        }else{
            System.out.println(((n+1)/2)/n);
        }
    }
}
