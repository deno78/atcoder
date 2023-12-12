import java.util.*;

public class Main{
    public static void main(String[] args){
        char[] c = new Scanner(System.in).next().toCharArray();
        Arrays.sort(c);
        System.out.println(
            (c[0]==c[1]&&c[2]==c[3]&&c[0]!=c[2])?
            "Yes":"No"
        );
    }
}