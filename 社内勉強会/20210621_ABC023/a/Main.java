import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String x = sc.next();
        int sum=0;
        for(Character c : x.toCharArray()){
            sum+=Integer.valueOf(c.toString());
        }
        System.out.println(sum);
    }
}
