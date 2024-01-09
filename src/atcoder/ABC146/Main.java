import java.util.*;

public class Main{
    public static void main(String[] args){
        List<String> list = Arrays.asList(new String[]{"SUN","MON","TUE","WED","THU","FRI","SAT" });
        String s = new Scanner(System.in).next();
        System.out.println(
            7-list.indexOf(s)
        );
        

    }
}