import java.util.*;
import jdk.jshell.*;
class Main{
    public static void main(String[] args){
        String line = new Scanner(System.in).nextLine().replace(" ","*");
        System.out.println(JShell.create().eval(line).stream().reduce((a,b)->b).map(SnippetEvent::value).orElse(null));
    }
}