import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        Map<Character,Integer> map = new HashMap<Character,Integer>();
        for(Character c : s.toCharArray()){
            if(!map.containsKey(c)){
                map.put(c,0);
            }
            map.put(c,map.get(c)+1);
        }
        if(map.size()!=2){
            System.out.println("No");
            System.exit(0);
        }
        for(Map.Entry<Character,Integer> ent:map.entrySet()){
            if(ent.getValue()!=2){
                System.out.println("No");
                System.exit(0);
            }
        }
        System.out.println("Yes");
    }
}