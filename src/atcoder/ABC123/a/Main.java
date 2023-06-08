import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        List<Integer> a = new ArrayList<Integer>();
        for(int i=0;i<6;i++){a.add(s.nextInt());}
        System.out.println((a.get(4)- a.get(0)> a.get(5))?":(":"Yay!");
    }
}