import java.util.*;

public class Main{
    public static void main(String[] args){
        String[] s = new Scanner(System.in).nextLine().split(" ");
        Set set = new HashSet(Arrays.asList(s));
        System.out.println(
            set.size()==2?"Yes":"No"
        );
    }
}