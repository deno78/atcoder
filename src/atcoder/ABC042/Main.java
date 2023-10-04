import java.util.*;

public class Main{
    public static void main(String[] args){
        String[] s = (String[]) new Scanner(System.in).nextLine().split(" ");
        Arrays.sort(s);        
        System.out.println(String.join("",s).equals("557")?"YES":"NO");
    }
}