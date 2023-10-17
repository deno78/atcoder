import java.util.*;

public class Main{
    public static void main(String[] args){
        String n = new Scanner(System.in).next();
        Set set = new HashSet<Character>();
        for(Character c : n.toCharArray()){
            set.add(c);
        }
        System.out.println(set.size()==1?"SAME":"DIFFERENT");
    }
}