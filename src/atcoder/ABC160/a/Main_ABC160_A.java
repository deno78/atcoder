import java.util.*;

public class Main_ABC160_A{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        if(s.toCharArray()[2]==s.toCharArray()[3] && s.toCharArray()[4]==s.toCharArray()[5]){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}