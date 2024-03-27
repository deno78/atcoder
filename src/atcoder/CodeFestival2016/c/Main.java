import java.util.*;

public class Main {
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        System.out.println(
            s.matches(".*C.*F.*")
            ?"Yes":"No");
    }
    
}
