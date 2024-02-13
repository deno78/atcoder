import java.util.*;

class Main {
    public static void main(String[] args)throws Exception{
        char c = new Scanner(System.in).next().charAt(0);
        System.out.printf("%c",
           'a'+ (c-Character.toLowerCase(c))
        );
    }
}
